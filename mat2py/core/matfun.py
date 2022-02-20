# type: ignore
from mat2py.common.backends import linalg as _linalg
from mat2py.common.backends import numpy as np

from ._internal.array import M
from ._internal.helper import argout_wrapper_decorators


def eig(x, *args, nargout=2):
    if nargout != 2 or args:
        raise NotImplementedError("eig")
    D, V = _linalg.eig(x)
    return M[V], M[np.diag(D.reshape(-1))]


def normest(*args):
    raise NotImplementedError("normest")


def ordqz(*args):
    raise NotImplementedError("ordqz")


def lscov(*args):
    raise NotImplementedError("lscov")


def qrinsert(*args):
    raise NotImplementedError("qrinsert")


def trace(*args):
    raise NotImplementedError("trace")


def ishermitian(*args):
    raise NotImplementedError("ishermitian")


def pinv(*args):
    raise NotImplementedError("pinv")


def gsvd(*args):
    raise NotImplementedError("gsvd")


def condest(*args):
    raise NotImplementedError("condest")


def polyeig(*args):
    raise NotImplementedError("polyeig")


def rcond(*args):
    raise NotImplementedError("rcond")


def norm(*args):
    raise NotImplementedError("norm")


def hess(*args):
    raise NotImplementedError("hess")


def condeig(*args):
    raise NotImplementedError("condeig")


def bandwidth(*args):
    raise NotImplementedError("bandwidth")


def ltitr(*args):
    raise NotImplementedError("ltitr")


def funm(*args):
    raise NotImplementedError("funm")


def qz(*args):
    raise NotImplementedError("qz")


def istriu(*args):
    raise NotImplementedError("istriu")


def isbanded(*args):
    raise NotImplementedError("isbanded")


def logm(*args):
    raise NotImplementedError("logm")


def sqrtm(*args):
    raise NotImplementedError("sqrtm")


def rsf2csf(*args):
    raise NotImplementedError("rsf2csf")


def cond(*args):
    raise NotImplementedError("cond")


def qrupdate(*args):
    raise NotImplementedError("qrupdate")


inv = argout_wrapper_decorators()(np.linalg.inv)


def det(*args):
    raise NotImplementedError("det")


def cdf2rdf(*args):
    raise NotImplementedError("cdf2rdf")


def cholupdate(*args):
    raise NotImplementedError("cholupdate")


def schur(*args):
    raise NotImplementedError("schur")


def balance(*args):
    raise NotImplementedError("balance")


def expm(*args):
    raise NotImplementedError("expm")


def normest1(*args):
    raise NotImplementedError("normest1")


def isdiag(*args):
    raise NotImplementedError("isdiag")


def ldl(*args):
    raise NotImplementedError("ldl")


def ordschur(*args):
    raise NotImplementedError("ordschur")


def svd(*args):
    raise NotImplementedError("svd")


def istril(*args):
    raise NotImplementedError("istril")


def lu(*args):
    raise NotImplementedError("lu")


def qr(*args):
    raise NotImplementedError("qr")


def planerot(*args):
    raise NotImplementedError("planerot")


def chol(*args):
    raise NotImplementedError("chol")


def orth(*args):
    raise NotImplementedError("orth")


def null(*args):
    raise NotImplementedError("null")


def ordeig(*args):
    raise NotImplementedError("ordeig")


def sylvester(*args):
    raise NotImplementedError("sylvester")


def issymmetric(*args):
    raise NotImplementedError("issymmetric")


def rref(*args):
    raise NotImplementedError("rref")


def linsolve(*args):
    raise NotImplementedError("linsolve")


def qrdelete(*args):
    raise NotImplementedError("qrdelete")


def rank(*args):
    raise NotImplementedError("rank")
