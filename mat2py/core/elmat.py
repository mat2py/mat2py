# type: ignore
__all__ = [
    "nan",
    "NaN",
    "pi",
    "i",
    "j",
    "true",
    "false",
    "eps",
    "inf",
    "realmin",
    "reshape",
    "accumarray",
    "ndims",
    "isvector",
    "gallery",
    "eye",
    "isinf",
    "flipud",
    "length",
    "fliplr",
    "tril",
    "rosser",
    "flipdim",
    "hankel",
    "hadamard",
    "diag",
    "vander",
    "hilb",
    "squeeze",
    "numel",
    "ndgrid",
    "peaks",
    "iscolumn",
    "repmat",
    "cat",
    "wilkinson",
    "isequaln",
    "freqspace",
    "pascal",
    "isfinite",
    "sub2ind",
    "intmax",
    "isrow",
    "meshgrid",
    "compan",
    "permute",
    "size",
    "invhilb",
    "realmax",
    "flip",
    "zeros",
    "shiftdim",
    "repelem",
    "ismatrix",
    "flintmax",
    "logspace",
    "isempty",
    "isscalar",
    "magic",
    "ipermute",
    "blkdiag",
    "ones",
    "ind2sub",
    "find",
    "triu",
    "intmin",
    "isnan",
    "isequalwithequalnans",
    "linspace",
    "bsxfun",
    "rot90",
    "circshift",
    "isequal",
    "toeplitz",
]


import functools

from mat2py.common.backends import linalg as _linalg
from mat2py.common.backends import numpy as np
from mat2py.common.backends import py_all

from ._internal.array import (
    M,
    ind2sub,
    mp_can_cast_to_number,
    mp_convert_round,
    mp_convert_scalar,
)
from ._internal.cell import CellArray
from ._internal.helper import (
    mp_argout_wrapper_decorators,
    mp_inference_nargout_decorators,
    mp_last_arg_as_kwarg,
    mp_match_vector_direction,
    mp_nargout_from_stack,
    mp_special_variables,
)
from ._internal.math_helper import mp_zeros_like_decorators
from ._internal.struct import StructArray, mp_fieldnames_list


def realmin(*args):
    raise NotImplementedError("realmin")


def reshape(x, *args):
    if len(args) == 1 and isinstance(args[0], np.ndarray) and np.size(args[0]) > 0:
        return x.reshape(args[0].reshape(-1).astype(int), order="F")
    else:
        shape = tuple(-1 if np.size(i) == 0 else i for i in args)
        return x.reshape(shape, order="F")

    raise NotImplementedError("reshape")


nan = mp_special_variables(np.nan)
NaN = nan


def accumarray(*args):
    raise NotImplementedError("accumarray")


def ndims(*args):
    raise NotImplementedError("ndims")


def isvector(a):
    if np.ndim(a) == 2:
        return np.min(np.shape(a)) <= 1
    return np.ndim(a) < 2


def gallery(*args):
    raise NotImplementedError("gallery")


eye = mp_zeros_like_decorators(expand_shape=True)(np.eye)


i = mp_special_variables(1j)


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


j = mp_special_variables(1j)


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


true = mp_special_variables(True)


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


def meshgrid(x, *args, nargout=None):
    if nargout is None:
        nargout = mp_nargout_from_stack()

    if nargout != 1 + len(args):
        assert len(args) == 0
        args = (x,) * (nargout - 1)

    return tuple(M[i] for i in np.meshgrid(x, *args))


eps = mp_special_variables(np.finfo(float).eps)


def compan(*args):
    raise NotImplementedError("compan")


def permute(*args):
    raise NotImplementedError("permute")


pi = mp_special_variables(np.pi)


@mp_inference_nargout_decorators()
def size(a, *args, nargout=None):
    if args:
        (d,) = args
        d = mp_convert_scalar(mp_convert_round(d))
        assert d > 0
        return (np.shape(a)[d - 1],)
    shape = list(np.shape(a))
    if nargout == 1:
        if len(shape) == 0:
            return (M[[1, 1]],)
        if len(shape) == 1:
            return (M[[1, shape[0]]],)
        return (M[shape],)
    if nargout < len(shape):
        shape = [*shape[:nargout], np.prod(shape[nargout:])]
    elif nargout > len(shape):
        shape = [*shape, *([1] * (nargout - len(shape)))]
    return tuple(shape)


def invhilb(*args):
    raise NotImplementedError("invhilb")


def realmax(*args):
    raise NotImplementedError("realmax")


false = mp_special_variables(False)


def flip(*args):
    raise NotImplementedError("flip")


zeros = mp_zeros_like_decorators()(np.zeros)


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


def isempty(a):
    return M[int(np.size(a) == 0)]


def isscalar(*args):
    raise NotImplementedError("isscalar")


def magic(*args):
    raise NotImplementedError("magic")


def ipermute(*args):
    raise NotImplementedError("ipermute")


def blkdiag(*args):
    raise NotImplementedError("blkdiag")


ones = mp_zeros_like_decorators()(np.ones)


inf = mp_special_variables(np.inf)
Inf = inf


@mp_match_vector_direction()
@mp_last_arg_as_kwarg("direction", ("first", "last"))
def find(x, *args, direction="first", nargout=None):
    if nargout is None:
        nargout = mp_nargout_from_stack(4)

    if len(args) == 0:
        if nargout == 2:
            r, c = M[x].nonzero()
            ic = np.argsort(c)
            r, c = M[r[ic] + 1], M[c[ic] + 1]
            if np.ndim(x) >= 2 or np.shape(x)[0] > 1:
                r, c = r.reshape(-1, 1), c.reshape(-1, 1)
            return r, c

        ind = np.where(x)
        if x.ndim < 2:
            return M[ind[0].reshape((1, -1) if x.shape[0] == 1 else (-1, 1)) + 1]
        else:
            return M[np.sort(ind[0] + ind[1] * x.shape[0] + 1).reshape(-1, 1)]

    assert len(args) == 1
    n = mp_convert_scalar(mp_convert_round(args[0]))
    assert n > 0
    # TODO: improve this slow implementation
    res = find(x, nargout=nargout)

    if direction == "first":
        return res[:n] if nargout == 1 else (res[0][:n], res[1][:n])
    else:
        return res[-n:] if nargout == 1 else (res[0][-n:], res[1][-n:])


def triu(*args):
    raise NotImplementedError("triu")


def intmin(*args):
    raise NotImplementedError("intmin")


isnan = np.isnan


def isequalwithequalnans(*args):
    raise NotImplementedError("isequalwithequalnans")


@mp_argout_wrapper_decorators()
def linspace(*args):
    return np.linspace(*args)


def bsxfun(fun, a, b):
    # np.random.randint(0,1, tuple(np.maximum(da, db)*(1 if da>0 and db>0 else 0) for da, db in zip(a.shape, b.shape))).astype(np.bool)
    return M[fun(a, b)]


def rot90(*args):
    raise NotImplementedError("rot90")


def circshift(*args):
    raise NotImplementedError("circshift")


def isequal(*args):
    assert len(args) > 1
    if len(args) == 2:
        a, b = args
        if isinstance(a, StructArray):
            if not isinstance(b, StructArray):
                return False
            an, bn = map(mp_fieldnames_list, args)
            names = {*an, *bn}
            if len(an) == len(bn) and len(an) == len(names):
                return py_all(isequal(a[n], b[n]) for n in names)
            return False

        if mp_can_cast_to_number(a):
            if not mp_can_cast_to_number(b):
                return False
            a = M[a]
            b = M[b]

        if isinstance(a, np.ndarray):
            if not isinstance(b, np.ndarray):
                return False
            return a.shape == b.shape and np.all(a == b)
        raise NotImplementedError

    return py_all(isequal(i, j) for i, j in zip(args[:-1], args[1:]))


toeplitz = mp_argout_wrapper_decorators()(_linalg.toeplitz)
