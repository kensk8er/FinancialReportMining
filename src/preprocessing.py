"""
Preprocessing text
"""
import logging
import string
from gensim import corpora
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
import re
from module.text.compoundword import compound_words
from module.text.stopword import extended_stopwords
from utils.util import unpickle, enpickle

__author__ = 'kensk8er'


def get_tokens(text):
    lowers = text.lower()
    no_punctuation = lowers.translate(None, string.punctuation)
    return word_tokenize(no_punctuation)


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        # return NOUN if others
        return wordnet.NOUN


def convert_compound(document):
    doc_string = " ".join(document)
    for compound_word in compound_words:
        doc_string = re.sub(compound_word, re.sub('\s', '-', compound_word), doc_string)

    return doc_string.split()


def clean_text(text):
    text = re.sub("(http(s)?://[A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]+)", '', text)  # URL
    text = re.sub("(www\.[A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]+)", '', text)  # URL
    text = re.sub("([A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]+\.\w+)", '', text)  # URL
    text = re.sub("(\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6})", '', text)  # email
    text = re.sub("(-{2,})", '', text)  # hyphen
    text = re.sub("(\w+)(-)(\w+)", r'\1 \3', text)  # hyphen
    text = re.sub("(mailto:\w+)", r'\1 \3', text)  # hyphen
    text = re.sub("=\r\n", '', text)  # next-line
    text = re.sub("([A-Za-z0-9\'~+\-=_.,/%\?!;:@#\*&\(\)]{15,})", '', text)  # long characters
    text = re.sub("(\b)(\w)(\b)", r'\1 \3', text)  # short (single) characters
    text = re.sub("[0-9]", '', text)  # number
    return text


if __name__ == '__main__':
    # hyper-parameters
    noun_only = True
    max_doc = float('inf')
    title_weight = 3

    # logging
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.DEBUG)

    # expand stopwords list
    stop_words = extended_stopwords

    logging.info('load documents...')
    documents = unpickle('data/txt/documents.pkl')
    lemmatizer = WordNetLemmatizer()

    logging.info('lemmatize...')
    count = 0
    doc_num = len(documents)
    new_documents = []
    titles = []
    froms = []
    dates = []
    for index, document in documents.items():
        count += 1
        if count > max_doc:
            break

        print '\r', count, '/', doc_num,
        text = document['text'] + (' ' + index) * title_weight
        from_name = document['from']
        date = document['date']

        # delete irrelevant characters
        text = clean_text(text)

        tokens = get_tokens(text)
        filtered = [w for w in tokens if not w in stop_words]
        tagged = pos_tag(filtered)

        document = []
        for word in tagged:
            tag = get_wordnet_pos(word[1])

            # process NOUN only if noun_only is True
            if noun_only is False or tag == wordnet.NOUN:
                if len(word[0]) >= 2:
                    document.append(lemmatizer.lemmatize(word[0], pos=tag))

        # convert compound word into one token
        document = convert_compound(document)

        new_documents.append(document)
        titles.append(index)
        froms.append(from_name)
        dates.append(date)

    print '\n'
    logging.info('create dictionary and corpus...')
    dictionary = corpora.Dictionary(new_documents)
    dictionary.docid2title = titles
    dictionary.docid2from = froms
    dictionary.docid2date = dates

    logging.info('filter unimportant words...')
    dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=None)
    dictionary.compactify()

    logging.info('generate corpus...')
    dictionary.corpus = [dictionary.doc2bow(document) for document in new_documents]

    if noun_only is True:
        dictionary.save('data/dictionary/noun_dictionary.dict')
    else:
        dictionary.save('data/dictionary/dictionary.dict')
