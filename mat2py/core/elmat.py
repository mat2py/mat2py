# type: ignore
from ._internal.array import M, ind2sub
from ._internal.helper import matlab_function_decorators, special_variables
from ._internal.package_proxy import numpy as np


def realmin(*args):
    raise NotImplementedError("realmin")


def reshape(*args):
    raise NotImplementedError("reshape")


nan = special_variables(np.nan)
NaN = nan


def accumarray(*args):
    raise NotImplementedError("accumarray")


def ndims(*args):
    raise NotImplementedError("ndims")


def isvector(*args):
    raise NotImplementedError("isvector")


def gallery(*args):
    raise NotImplementedError("gallery")


def eye(*args):
    raise NotImplementedError("eye")


i = special_variables(1j)


def isinf(*args):
    raise NotImplementedError("isinf")


def flipud(*args):
    raise NotImplementedError("flipud")


def length(*args):
    raise NotImplementedError("length")


def fliplr(*args):
    raise NotImplementedError("fliplr")


def tril(*args):
    raise NotImplementedError("tril")


def rosser(*args):
    raise NotImplementedError("rosser")


def flipdim(*args):
    raise NotImplementedError("flipdim")


def hankel(*args):
    raise NotImplementedError("hankel")


def hadamard(*args):
    raise NotImplementedError("hadamard")


def diag(*args):
    raise NotImplementedError("diag")


def vander(*args):
    raise NotImplementedError("vander")


def hilb(*args):
    raise NotImplementedError("hilb")


def squeeze(*args):
    raise NotImplementedError("squeeze")


def numel(a):
    return np.size(a)


j = special_variables(1j)


def ndgrid(*nd):
    return tuple(M[i].T for i in np.meshgrid(*nd))


def peaks(*args):
    raise NotImplementedError("peaks")


def iscolumn(*args):
    raise NotImplementedError("iscolumn")


def repmat(*args):
    raise NotImplementedError("repmat")


def cat(*args):
    raise NotImplementedError("cat")


def wilkinson(*args):
    raise NotImplementedError("wilkinson")


def isequaln(*args):
    raise NotImplementedError("isequaln")


def freqspace(*args):
    raise NotImplementedError("freqspace")


true = special_variables(True)


def pascal(*args):
    raise NotImplementedError("pascal")


def isfinite(*args):
    raise NotImplementedError("isfinite")


def sub2ind(*args):
    raise NotImplementedError("sub2ind")


def intmax(*args):
    raise NotImplementedError("intmax")


def isrow(*args):
    raise NotImplementedError("isrow")


def meshgrid(*args):
    raise NotImplementedError("meshgrid")


eps = special_variables(np.finfo(float).eps)


def compan(*args):
    raise NotImplementedError("compan")


def permute(*args):
    raise NotImplementedError("permute")


pi = special_variables(np.pi)


def size(a):
    if np.size(a) == 1 and np.ndim(a) < 2:
        return 1, 1
    else:
        return np.shape(a)


def invhilb(*args):
    raise NotImplementedError("invhilb")


def realmax(*args):
    raise NotImplementedError("realmax")


false = special_variables(False)


def flip(*args):
    raise NotImplementedError("flip")


def zeros(*args):
    raise NotImplementedError("zeros")


def shiftdim(*args):
    raise NotImplementedError("shiftdim")


def repelem(*args):
    raise NotImplementedError("repelem")


def ismatrix(*args):
    raise NotImplementedError("ismatrix")


def flintmax(*args):
    raise NotImplementedError("flintmax")


def logspace(*args):
    raise NotImplementedError("logspace")


def isempty(*args):
    raise NotImplementedError("isempty")


def isscalar(*args):
    raise NotImplementedError("isscalar")


def magic(*args):
    raise NotImplementedError("magic")


def ipermute(*args):
    raise NotImplementedError("ipermute")


def blkdiag(*args):
    raise NotImplementedError("blkdiag")


def ones(*args):
    raise NotImplementedError("ones")


inf = special_variables(np.inf)
Inf = inf


def find(*args):
    raise NotImplementedError("find")


def triu(*args):
    raise NotImplementedError("triu")


def intmin(*args):
    raise NotImplementedError("intmin")


def isnan(*args):
    raise NotImplementedError("isnan")


def isequalwithequalnans(*args):
    raise NotImplementedError("isequalwithequalnans")


@matlab_function_decorators()
def linspace(*args):
    return np.linspace(*args)


def bsxfun(*args):
    raise NotImplementedError("bsxfun")


def rot90(*args):
    raise NotImplementedError("rot90")


def circshift(*args):
    raise NotImplementedError("circshift")


def isequal(*args):
    raise NotImplementedError("isequal")


def toeplitz(*args):
    raise NotImplementedError("toeplitz")
