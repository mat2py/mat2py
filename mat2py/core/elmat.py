# type: ignore
import functools

from mat2py.common.backends import linalg as _linalg
from mat2py.common.backends import numpy as np

from ._internal.array import M, _convert_round, _convert_scalar, ind2sub
from ._internal.helper import argout_wrapper_decorators, special_variables


@functools.lru_cache(maxsize=10)
def _zeros_like_decorators(expand_shape=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            args = tuple(_convert_scalar(i) for i in args)
            dtype = np.float_
            shape = args
            if len(args) >= 2 and args[-2] == "like":
                dtype = M[args[-1]].dtype
                shape = args[:-2]
            elif isinstance(args[-1], str):
                classname = args[-1]
                dtype = {
                    "double": np.float64,
                    "single": np.float32,
                }.get(classname, getattr(np, classname))
                shape = args[:-1]

            if len(shape) == 0:
                shape = (1, 1)
            elif len(shape) == 1 and isinstance(shape[0], np.ndarray):
                shape = shape[0].reshape(-1).tolist()
            elif len(shape) == 1:
                shape = (shape[0], shape[0])
            shape = tuple(_convert_round(s) for s in shape)
            if expand_shape:
                return M[func(*shape, dtype=dtype)]
            else:
                return M[func(shape, dtype=dtype)]

        return wrapper

    return decorator


def realmin(*args):
    raise NotImplementedError("realmin")


def reshape(x, *args):
    if len(args) == 1 and isinstance(args[0], np.ndarray) and np.size(args[0]) > 0:
        return x.reshape(tuple(i for i in args[0]), order="F")
    else:
        shape = tuple(-1 if np.size(i) == 0 else i for i in args)
        return x.reshape(shape, order="F")

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


eye = _zeros_like_decorators(expand_shape=True)(np.eye)


i = special_variables(1j)


def isinf(*args):
    raise NotImplementedError("isinf")


def flipud(*args):
    raise NotImplementedError("flipud")


def length(x):
    return np.max(np.size(x))


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


def diag(x, *args):
    if args:
        raise NotImplementedError("diag")
    else:
        if np.ndim(x) > 2:
            raise ValueError("First input must be 2-D.")

        if np.max(np.shape(x)) == np.size(x):
            return M[np.diag(x.reshape(-1))]
        else:
            return M[np.diag(x).reshape(-1, 1)]


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


zeros = _zeros_like_decorators()(np.zeros)


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


ones = _zeros_like_decorators()(np.ones)


inf = special_variables(np.inf)
Inf = inf


def find(x, *args, nargout=None):
    if nargout is None:
        # ToDo: use inspect to get stack for nargout?
        nargout = 2

    if nargout == 2:
        return tuple(M[i] + 1 for i in M[x].nonzero())

    if len(args) == 0:
        ind = np.where(x)
        if x.ndim < 2:
            return ind[0].reshape((1, -1) if x.shape[0] == 1 else (-1, 1)) + 1
        else:
            return np.sort(ind[0] + ind[1] * x.shape[0] + 1).reshape(-1, 1)

    raise NotImplementedError("find")


def triu(*args):
    raise NotImplementedError("triu")


def intmin(*args):
    raise NotImplementedError("intmin")


def isnan(*args):
    raise NotImplementedError("isnan")


def isequalwithequalnans(*args):
    raise NotImplementedError("isequalwithequalnans")


@argout_wrapper_decorators()
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


toeplitz = argout_wrapper_decorators()(_linalg.toeplitz)
