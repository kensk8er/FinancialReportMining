"""
Specify topics to extract knowledge from wikipedia.
"""
from gensim.models import LdaModel
import numpy as np

__author__ = 'kensk8er'


def get_keywords(threshold=0.01, model_path='result/model.lda'):
    lda_model = LdaModel.load(model_path)
    topic_num = lda_model.num_topics
    keywords = set()
    for topic_id in range(topic_num):
        topic = lda_model.state.get_lambda()[topic_id]
        topic = topic / topic.sum()  # normalize to probability dist
        signif_word_ids = np.where(topic > threshold)[0]
        keywords = keywords.union([lda_model.id2word[word_id] for word_id in signif_word_ids])

    return keywords


# hand-selected keywords (not used currently)
keywords = {'season', 'drag', 'delay', 'respondent', 'farm', 'hawk', 'wait', 'vail', 'strat', 'cli', 'signal', 'ratio',
          'wave', 'sequential', 'saar', 'correction', 'trend', 'principle', 'trading', 'charge', 'economic', 'scenario',
          'uncertainty', 'framework', 'challenge', 'implication', 'troika', 'shock', 'implementation', 'style', 'ec',
          'german', 'authority', 'law', 'joh', 'gossler', 'qoq', 'employee', 'germany', 'mistake', 'credit', 'spread',
          'bp', 'default', 'loss', 'bps', 'ig', 'issuance', 'bond', 'sector', 'bn', 'buying', 'momentum', 'usd',
          'toshin', 'mn', 'purchase', 'sale', 'row', 'investing', 'currency', 'usd', 'fx', 'eur', 'aud', 'gbp', 'band',
          'score', 'cny', 'edge', 'pt', 'tech', 'healthcare', 'utility', 'technology', 'energy', 'chemical', 'meeting',
          'st', 'medium', 'election', 'party', 'poll', 'result', 'government', 'seat', 'parliament', 'support',
          'majority', 'coalition', 'loan', 'dot', 'funding', 'deposit', 'shadow', 'summer', 'cds', 'composite',
          'homebuilder', 'visa', 'payroll', 'income', 'ism', 'change', 'weather', 'employment', 'point', 'pdf',
          'difficulty', 'datum', 'siemens', 'london', 'closing', 'seller', 'soe', 'kiev', 'ge', 'haven', 'thai',
          'exercise', 'minister', 'greece', 'party', 'greek', 'commission', 'parliament', 'labour', 'finance',
          'president', 'nemo', 'home', 'sale', 'leverage', 'optimism', 'faith', 'affordability', 'south', 'pending',
          'fallout', 'peak', 'bp', 'yr', 'swap', 'trade', 'australia', 'spread', 'yield', 'rba', 'bias', 'level',
          'meeting', 'guidance', 'committee', 'yellen', 'fomc', 'slack', 'fed', 'statement', 'official', 'fund',
          'episode', 'wealth', 'law', 'phillip', 'mericle', 'sale', 'management', 'corporation', 'insurance', 'banking',
          'china', 'gavekal', 'america', 'dragonomic', 'team', 'entity', 'review', 'trouble', 'idea', 'dissemination',
          'gold', 'metal', 'trading', 'platinum', 'strike', 'palladium', 'support', 'silver', 'commodity', 'koz',
          'consumer', 'confidence', 'sentiment', 'summit', 'publication', 'component', 'consensus', 'economist', 'drop',
          'business', 'property', 'china', 'telecom', 'construction', 'ore', 'iron', 'financial', 'developer', 'sector',
          'cement', 'volatility', 'eur', 'ecb', 'bund', 'eonia', 'vol', 'differential', 'bps', 'option', 'spread',
          'brl', 'sterling', 'unch', 'macro', 'mxn', 'datum', 'itx', 'change', 'vix', 'euro', 'rating', 'economic',
          'date', 'publication', 'boe', 'carney', 'independence', 'credit', 'uk', 'referendum', 'turkey',
          'south-africa', 'rating', 'dm', 'stock', 'structure', 'allocation', 'event', 'poland', 'factor', 'reserve',
          'commentary', 'transfer', 'customer', 'party', 'sterling', 'future', 'option', 'tick', 'paper', 'demand',
          'supply', 'text', 'contact', 'arbitrage', 'drife', 'repeat', 'synopsis', 'bulk', 'database', 'model',
          'change', 'projection', 'fix', 'contribution', 'pip', 'renminbi', 'error', 'basket', 'fig', 'regime',
          'dashboard', 'profitability', 'grade', 'panel', 'landing', 'banker', 'sustainability', 'vladimir',
          'ownership', 'vote', 'city', 'voting', 'family', 'centre', 'deadline', 'polling', 'income', 'investor',
          'performer', 'exchange', 'stock', 'overweight', 'india', 'singapore', 'hong-kong', 'authority', 'company',
          'china', 'japan', 'box', 'paper', 'cross', 'store', 'announcement', 'check', 'section', 'search', 'street',
          'consumer', 'mm', 'relief', 'mix', 'radar', 'favour', 'expected', 'consultation', 'htb', 'milk', 'optimism',
          'liquidity', 'money', 'balance-sheet', 'facility', 'reserve', 'operation', 'banking', 'condition', 'cash',
          'willingness', 'china', 'equity', 'macro', 'matter', 'fx', 'essential', 'credit', 'asia', 'latam', 'emea',
          'surprise', 'datum', 'activity', 'condition', 'cycle', 'weakness', 'momentum', 'point', 'level', 'pmis',
          'trade', 'unit', 'idea', 'loss', 'edition', 'sale', 'ppi', 'td', 'brussel', 'eu', 'ag', 'affiliate',
          'investor', 'instrument', 'law', 'capital', 'authority', 'branch', 'advice', 'subsidiary', 'commodity',
          'video', 'cycle', 'agriculture', 'premia', 'winner', 'metal', 'yielding', 'topic', 'analytic', 'premier',
          'breaking', 'promise', 'writing', 'foot', 'passenger', 'underwriting', 'bullet', 'oz', 'living',
          'unemployment', 'wage', 'employment', 'labor', 'labour', 'job', 'worker', 'force', 'decline', 'gain',
          'capacity', 'air', 'iraq', 'spirit', 'map', 'wine', 'pick', 'wholesaler', 'bust', 'isis', 'reform', 'capital',
          'stress', 'rule', 'deal', 'test', 'agreement', 'progress', 'renzi', 'exit', 'conference', 'congress',
          'senate', 'house', 'easter', 'replay', 'participant', 'chairman', 'vice', 'dial', 'claim', 'spring', 'volume',
          'mendelson', 'health', 'health-care', 'average', 'benefit', 'uptrend', 'rally', 'policy', 'hike', 'meeting',
          'path', 'tightening', 'hold', 'change', 'stance', 'decision', 'cut', 'company', 'transmission', 'virus',
          'responsibility', 'issuer', 'screen', 'notice', 'damage', 'reliance', 'request', 'auction', 'authority',
          'bond', 'issuance', 'regulation', 'treasury', 'jp', 'investor', 'exchange', 'conduct', 'china', 'asia',
          'policy', 'rmb', 'sector', 'pboc', 'stimulus', 'property', 'slowdown', 'easing', 'government', 'tax',
          'deficit', 'budget', 'gdp', 'debt', 'sector', 'cut', 'spending', 'finance', 'transaction', 'toll', 'trading',
          'swap', 'desk', 'df', 'condition', 'derivative', 'business', 'accumulation', 'uk', 'bst', 'st', 'median',
          'floor', 'japan', 'emu', 'san', 'london', 'axe', 'mr', 'eur', 'court', 'programme', 'head', 'austerity',
          'baseline', 'decision', 'reuter', 'door', 'issue', 'gap', 'way', 'level', 'fact', 'adjustment', 'approach',
          'case', 'step', 'rrr', 'publication', 'disclaimer', 'zone', 'case', 'code', 'environment', 'utilisation',
          'country', 'reader', 'diffusion', 'capex', 'print', 'earning', 'office', 'improvement', 'cos', 'transition',
          'transport', 'activity', 'upward', 'bond', 'debt', 'asset', 'investor', 'government', 'buying', 'capital',
          'currency', 'purchase', 'fdi', 'auto', 'sale', 'industrial', 'investor', 'vehicle', 'gm', 'department', 'bmw',
          'good', 'board', 'company', 'margin', 'earning', 'share', 'stock', 'revenue', 'business', 'management',
          'result', 'deal', 'economic', 'pgs', 'bs', 'llc', 'north-america', 'inflection', 'parker', 'repatriation',
          'vincent', 'drug', 'profile', 'london', 'portion', 'tracking', 'investor', 'relationship', 'england',
          'transaction', 'frequency', 'place', 'stock', 'sector', 'investor', 'value', 'exposure', 'return', 'equity',
          'strategist', 'valuation', 'beta', 'russia', 'ukraine', 'sanction', 'tension', 'crisis', 'europe', 'gas',
          'situation', 'escalation', 'eu', 'exhibit', 'country', 'impact', 'header', 'canada', 'period', 'effect',
          'example', 'level', 'africa', 'housing', 'household', 'mortgage', 'house', 'lending', 'ratio', 'credit',
          'boom', 'income', 'downturn', 'export', 'import', 'trade', 'demand', 'korea', 'economic', 'asia', 'good',
          'recovery', 'datum', 'dividend', 'downgrade', 'change', 'sa', 'andrea', 'ow', 'earning', 'apxj', 'insurance',
          'rating', 'pmi', 'manufacturing', 'production', 'order', 'output', 'sector', 'contraction', 'business',
          'level', 'car', 'yield', 'treasury', 'asset', 'level', 'participation', 'datum', 'premium', 'factor', 'yr',
          'shift', 'registration', 'banking', 'offering', 'united-states', 'issuer', 'vulnerability', 'sale', 'naira',
          'statement', 'jurisdiction', 'preview', 'watch', 'forum', 'inversion', 'club', 'mile', 'district',
          'litigation', 'mitsubishi', 'emission', 'pm', 'ukraine', 'imf', 'putin', 'region', 'referendum', 'president',
          'country', 'border', 'minister', 'thailand', 'infrastructure', 'surge', 'electricity', 'trip', 'water',
          'vietnam', 'project', 'barrier', 'axis', 'party', 'regulation', 'saudi-arabia', 'authority', 'msci', 'act',
          'affiliate', 'qatar', 'purpose', 'entity', 'industry', 'nikkei', 'look', 'building', 'ex', 'life', 'factory',
          'speaker', 'placement', 'piece', 'inflation', 'cpi', 'food', 'mpc', 'pressure', 'economic', 'energy',
          'effect', 'rise', 'level', 'order', 'deterioration', 'self', 'modi', 'series', 'answer', 'agenda',
          'reporting', 'venezuela', 'revolution', 'japan', 'boj', 'tax', 'hike', 'yen', 'easing', 'impact',
          'consumption', 'gpif', 'qe', 'ecb', 'inflation', 'measure', 'qe', 'policy', 'action', 'euro', 'draghi',
          'deposit', 'purchase', 'vs', 'duration', 'profit', 'gilt', 'income', 'belly', 'spread', 'opportunity', 'ukt',
          'trade', 'conference', 'press', 'kuroda', 'tone', 'tokyo', 'payback', 'room', 'sample', 'jgbs',
          'interpretation', 'guidance', 'pricing', 'york', 'new', 'takeaway', 'strength', 'opportunity', 'yield',
          'expense', 'track', 'figure', 'account', 'deficit', 'exchange', 'surplus', 'capital', 'key', 'correlation',
          'trade', 'appreciation', 'brazil', 'mexico', 'country', 'colombia', 'cad', 'argentina', 'em', 'latam',
          'chile', 'tracker', 'fund', 'inflow', 'outflow', 'flow', 'pension', 'investor', 'etfs', 'game', 'redemption',
          'beneficiary', 'germany', 'italy', 'france', 'spain', 'euro', 'german', 'country', 'eurozone', 'europe',
          'periphery', 'oil', 'gas', 'weekend', 'war', 'world', 'control', 'energy', 'threat', 'moscow', 'ground',
          'holding', 'pattern', 'advance', 'proportion', 'aqr', 'sapin', 'aversion', 'attractiveness', 'heart',
          'forecasting', 'mica', 'transmission', 'disclaimer', 'plc', 'template', 'economic', 'page', 'change', 'think',
          'addressee', 'macro', 'focus', 'list', 'europe', 'help', 'copper', 'team', 'basket', 'basis', 'headwind',
          'round', 'candidate', 'chance', 'interbank', 'talk', 'outcome', 'campaign', 'bid', 'president', 'leader',
          'sale', 'quarter', 'weather', 'consumer', 'datum', 'activity', 'indicator', 'inventory', 'good',
          'improvement', 'economy', 'recovery', 'crisis', 'economist', 'world', 'expansion', 'story', 'cost', 'sign',
          'recession', 'equity', 'msci', 'gem', 'earning', 'valuation', 'country', 'dm', 'egypt', 'outperformance',
          'stock', 'financial', 'event', 'pt', 'ms', 'commentary', 'ranking', 'aum', 'bps', 'beverage', 'afternoon',
          'debt', 'yy', 'gdp', 'giada', 'spain', 'guillaume', 'eu', 'pm', 'saunder', 'menuet', 'india', 'asia', 'rbi',
          'repo', 'subsidy', 'inr', 'indonesia', 'bjp', 'speaking', 'el', 'investor', 'firm', 'business', 'buyer',
          'factor', 'conflict', 'platform', 'objectivity', 'certification', 'channel', 'consensus', 'holiday',
          'governor', 'curf', 'trader', 'datum', 'ceemea', 'nigeria', 'distortion', 'davy', 'gdp', 'spending',
          'consumption', 'productivity', 'gain', 'revision', 'construction', 'economy', 'slowdown', 'sector'}
