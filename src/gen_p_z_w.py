"""
Generate P(z|w) out of P(w|z) and P(z).

P(w|z) and P(z) are generated by PLSA. P(z|w) indicates a weight of a word 'w' in a topic 'z', which is useful to
extract top-most n features in a topic.
"""
from utils.util import unpickle, enpickle
import numpy as np

__author__ = 'kensk8er'


def gen_p_w(p_w_z, p_z):
    """
    Generate P(w) out of P(w|z) and P(z).

    P(w) = Sigma_z[P(w|z) * P(z)]

    :param p_w_z: P(w|z)
    :param p_z: P(z)
    :return: P(w)
    """
    assert len(p_z.shape) == 1, 'p_z needs to be 1-dimensional!'
    assert len(p_w_z.shape) == 2, 'p_w_z needs to be 2-dimensional!'

    return p_w_z.dot(p_z)


def gen_p_wz(p_w_z, p_z):
    """
    Generate P(z,w) out of P(w|z) and P(z).

    P(z,w) = P(w|z) * P(z)

    :param p_w_z: P(w|z)
    :param p_z: P(z)
    :return: P(z,w)
    """
    return np.multiply(p_z, p_w_z)


def gen_p_z_w(p_wz, p_w):
    """
    Generate P(z|w) out of P(w,z), and P(w).

    Based on Bayes' rule: P(z|w) = P(w,z) / P(w)

    :param p_wz: P(z,w)
    :param p_w: P(w)
    :return: P(z|w)
    """
    return (p_wz / p_w.reshape((-1, 1))).T


if __name__ == '__main__':
    p_w_z = unpickle('result/plsa/p_w_z.pkl')
    p_z = unpickle('result/plsa/p_z.pkl')

    print 'computing P(w)...'
    p_w = gen_p_w(p_w_z, p_z)

    print 'computing P(z,w)...'
    p_wz = gen_p_wz(p_w_z, p_z)

    print 'computing P(z|w)...'
    p_z_w = gen_p_z_w(p_wz, p_w)

    print 'saving results into .pkl file...'
    enpickle(p_w, 'result/plsa/p_w.pkl')
    enpickle(p_wz, 'result/plsa/p_wz.pkl')
    enpickle(p_z_w, 'result/plsa/p_z_w.pkl')
