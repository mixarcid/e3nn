# pylint: disable=C,E1101
'''
Some functions related to SO3 and his usual representations

Using ZYZ Euler angles parametrisation
'''
import numpy as np


def rot_z(gamma):
    '''
    Rotation around Z axis
    '''
    return np.array([[np.cos(gamma), -np.sin(gamma), 0],
                     [np.sin(gamma), np.cos(gamma), 0],
                     [0, 0, 1]])


def rot_y(beta):
    '''
    Rotation around Y axis
    '''
    return np.array([[np.cos(beta), 0, np.sin(beta)],
                     [0, 1, 0],
                     [-np.sin(beta), 0, np.cos(beta)]])


def rot(alpha, beta, gamma):
    '''
    ZYZ Eurler angles rotation
    '''
    return rot_z(alpha).dot(rot_y(beta)).dot(rot_z(gamma))


def x_to_alpha_beta(x):
    x = x / np.linalg.norm(x)
    beta = np.arccos(x[2])
    alpha = np.arctan2(x[1], x[0])
    return (alpha, beta)


def dim(R):
    return R(0, 0, 0).shape[0]

# The next functions are some usual representations


def scalar_repr(alpha, beta, gamma):  # pylint: disable=W0613
    return np.array([[1]])


def vector_repr(alpha, beta, gamma):
    return rot(alpha, beta, gamma)


def tensor_repr(alpha, beta, gamma):
    r = vector_repr(alpha, beta, gamma)
    return np.kron(r, r)


def wigner_repr(l):
    from lie_learn.representations.SO3.wigner_d import wigner_D_matrix
    def func(alpha, beta, gamma):
        return wigner_D_matrix(l, alpha, beta, gamma)
    return func
