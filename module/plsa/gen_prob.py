"""
Generate P(w|z), P(w|z), P(w|z), and P(w|z).

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


def gen_p_w_z_w(p_w_z, p_w):
    """
    Generate P(w|z) / P(w) out of P(w|z) and P(w)
    :param p_w_z: P(w|z)
    :param p_w: P(w)
    :return: P(w|z) / P(w)
    """
    return p_w_z / p_w.reshape((-1, 1))


def gen_p_d(p_d_z, p_z):
    """
    Generate P(d) out of P(d|z) and P(z).

    P(d) = Sigma_z[P(d|z) * P(z)]

    :param p_d_z: P(d|z)
    :param p_z: P(z)
    :return: P(d)
    """
    assert len(p_z.shape) == 1, 'p_z needs to be 1-dimensional!'
    assert len(p_d_z.shape) == 2, 'p_d_z needs to be 2-dimensional!'

    return p_d_z.dot(p_z)


def gen_p_dz(p_d_z, p_z):
    """
    Generate P(z,d) out of P(d|z) and P(z).

    P(z,d) = P(d|z) * P(z)

    :param p_d_z: P(d|z)
    :param p_z: P(z)
    :return: P(z,d)
    """
    return np.multiply(p_z, p_d_z)


def gen_p_z_d(p_dz, p_d):
    """
    Generate P(z|d) out of P(d,z), and P(d).

    Based on Bayes' rule: P(z|d) = P(d,z) / P(d)

    :param p_dz: P(z,d)
    :param p_d: P(d)
    :return: P(z|d)
    """
    return (p_dz / p_d.reshape((-1, 1))).T


if __name__ == '__main__':
    p_w_z = unpickle('result/plsa/p_w_z.pkl')
    p_d_z = unpickle('result/plsa/p_d_z.pkl')
    p_z = unpickle('result/plsa/p_z.pkl')

    print 'computing P(w)...'
    p_w = gen_p_w(p_w_z, p_z)

    print 'computing P(z,w)...'
    p_wz = gen_p_wz(p_w_z, p_z)

    print 'computing P(z|w)...'
    p_z_w = gen_p_z_w(p_wz, p_w)

    print 'computing P(w|z) / P(w) = P(z,w) / {P(z) * P(w)}...'
    p_w_z_w = gen_p_w_z_w(p_w_z, p_w)

    print 'computing P(d)...'
    p_d = gen_p_d(p_d_z, p_z)

    print 'computing P(z,d)...'
    p_dz = gen_p_dz(p_d_z, p_z)

    print 'computing P(z|d)...'
    p_z_d = gen_p_z_d(p_dz, p_d)

    print 'saving results into .pkl file...'
    enpickle(p_w, 'result/plsa/p_w.pkl')
    enpickle(p_wz, 'result/plsa/p_wz.pkl')
    enpickle(p_z_w, 'result/plsa/p_z_w.pkl')
    enpickle(p_w_z_w, 'result/plsa/p_w_z_w.pkl')
