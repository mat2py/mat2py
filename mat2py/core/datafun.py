# type: ignore

__all__ = [
    "mode",
    "cumsum",
    "fftw",
    "trapz",
    "diff",
    "sum",
    "max",
    "cumtrapz",
    "mean",
    "ifft2",
    "filter2",
    "median",
    "cummax",
    "conv2",
    "fft2",
    "sort",
    "histcounts2",
    "histc",
    "discretize",
    "std",
    "conv",
    "filter",
    "cov",
    "min",
    "corrcoef",
    "hist",
    "fft",
    "ifftn",
    "del2",
    "cummin",
    "subspace",
    "deconv",
    "fftshift",
    "var",
    "gradient",
    "ifftshift",
    "issorted",
    "cumprod",
    "histcounts",
    "fftn",
    "prod",
    "ifft",
    "convn",
    "sortrows",
    "detrend",
]


import functools

from mat2py.common.backends import numpy as np

from ._internal.array import (
    M,
    mp_can_cast_to_scalar,
    mp_convert_round,
    mp_convert_scalar,
)
from ._internal.math_helper import mp_max_like_decorators, mp_sum_like_decorators

sum = mp_sum_like_decorators(default_if_empty=0)(np.sum)
prod = mp_sum_like_decorators(default_if_empty=1)(np.prod)
mean = mp_sum_like_decorators()(np.mean)
median = mp_sum_like_decorators()(np.median)
max = mp_max_like_decorators()(np.amax, np.argmax, np.maximum, np.nanmax, name="max")
min = mp_max_like_decorators()(np.amin, np.argmin, np.minimum, np.nanmin, name="min")


def mode(*args):
    raise NotImplementedError("mode")


def cumsum(*args):
    raise NotImplementedError("cumsum")


def fftw(*args):
    raise NotImplementedError("fftw")


def trapz(Y, *args):
    X = None
    dim = None
    dx = 1.0

    if len(args) == 2:
        X, Y, dim = (Y, *args)
    if len(args) == 1:
        if mp_can_cast_to_scalar(args[0]):
            dim = args[0]
        else:
            X, Y = Y, args[0]

    if dim is not None:
        dim = mp_convert_scalar(mp_convert_round(dim)) - 1
    else:
        dim = next(i for i, d in enumerate(np.shape(Y)) if d > 1)

    if X is not None:
        if mp_can_cast_to_scalar(X):
            X, dx = None, mp_convert_scalar(X)
        else:
            X = X.reshape(-1)

    return M[np.trapz(Y, X, dx, dim)]


def diff(a):
    if np.size(a) == 0:
        return M[np.zeros_like(a)]
    d = next(d for d, s in enumerate(np.shape(a)) if s > 1)
    return M[np.diff(a, axis=d)]


def cumtrapz(*args):
    raise NotImplementedError("cumtrapz")


def ifft2(*args):
    raise NotImplementedError("ifft2")


def filter2(*args):
    raise NotImplementedError("filter2")


def cummax(*args):
    raise NotImplementedError("cummax")


def conv2(*args):
    raise NotImplementedError("conv2")


def fft2(*args):
    raise NotImplementedError("fft2")


def sort(a, *args, nargout=1):
    if np.size(a) < 2:
        return a
    order = "ascend"
    args = [mp_convert_scalar(i) for i in args]
    if len(args) > 0 and isinstance(args[-1], str):
        order = args[-1]
        args = args[:-1]
    if len(args) > 0:
        dim = args[0]
    else:
        dim = [i for i, s in enumerate(np.shape(a)) if s > 1]
        dim = dim[0] if len(dim) > 0 else 0
    res = M[np.sort(a, dim)]
    if order == "descend":
        res = np.flip(res, dim)

    if nargout == 1:
        return res
    else:
        raise NotImplementedError


def histcounts2(*args):
    raise NotImplementedError("histcounts2")


def histc(*args):
    raise NotImplementedError("histc")


def discretize(*args):
    raise NotImplementedError("discretize")


def std(*args):
    raise NotImplementedError("std")


def conv(*args):
    raise NotImplementedError("conv")


def filter(*args):
    raise NotImplementedError("filter")


def cov(*args):
    raise NotImplementedError("cov")


def corrcoef(*args):
    raise NotImplementedError("corrcoef")


def hist(*args):
    raise NotImplementedError("hist")


def fft(*args):
    raise NotImplementedError("fft")


def ifftn(*args):
    raise NotImplementedError("ifftn")


def del2(*args):
    raise NotImplementedError("del2")


def cummin(*args):
    raise NotImplementedError("cummin")


def subspace(*args):
    raise NotImplementedError("subspace")


def deconv(*args):
    raise NotImplementedError("deconv")


def fftshift(*args):
    raise NotImplementedError("fftshift")


def var(*args):
    raise NotImplementedError("var")


def gradient(*args):
    raise NotImplementedError("gradient")


def ifftshift(*args):
    raise NotImplementedError("ifftshift")


def issorted(*args):
    raise NotImplementedError("issorted")


def cumprod(*args):
    raise NotImplementedError("cumprod")


def histcounts(*args):
    raise NotImplementedError("histcounts")


def fftn(*args):
    raise NotImplementedError("fftn")


def ifft(*args):
    raise NotImplementedError("ifft")


def convn(*args):
    raise NotImplementedError("convn")


def sortrows(*args):
    raise NotImplementedError("sortrows")


def detrend(*args):
    raise NotImplementedError("detrend")
