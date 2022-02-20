# type: ignore
import functools

from mat2py.common.backends import numpy as np

from ._internal.array import M, _convert_round, _convert_scalar


@functools.lru_cache(maxsize=10)
def _sum_like_decorators(default_if_empty=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(x, *args):
            if args and isinstance(args[-1], str):
                raise NotImplementedError
            if np.size(x) == 0 and default_if_empty is not None:
                return default_if_empty
            dim = (
                _convert_scalar(args[0]) - 1 if args else np.argmax(M[np.shape(x)] > 1)
            )
            res = func(x, _convert_round(dim), keepdims=True)
            r = np.argmax(np.array(np.shape(res))[::-1] > 1)
            if r > 0 and np.ndim(x) - r > 1:
                res = res.reshape(res.shape[:-r])
            return M[res]

        return wrapper

    return decorator


sum = _sum_like_decorators(default_if_empty=0)(np.sum)
prod = _sum_like_decorators(default_if_empty=1)(np.prod)
(
    max,
    min,
    mean,
    median,
) = (_sum_like_decorators()(f) for f in (np.max, np.min, np.mean, np.median))


def mode(*args):
    raise NotImplementedError("mode")


def cumsum(*args):
    raise NotImplementedError("cumsum")


def fftw(*args):
    raise NotImplementedError("fftw")


def trapz(*args):
    raise NotImplementedError("trapz")


def diff(*args):
    raise NotImplementedError("diff")


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
    args = [_convert_scalar(i) for i in args]
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
