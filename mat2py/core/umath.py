# type: ignore
from typing import Callable

import functools

import numpy as np

from .array import M


@functools.lru_cache(maxsize=10)
def matlab_function_decorators(nargout: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            obj = func(*args, **kwargs)
            if nargout == 1:
                return M[obj]
            else:
                raise NotImplementedError

        return wrapper

    return decorator


pi = np.pi
eps = np.finfo(float).eps


clc = None
clear = None
disp = print
error = print


def ndgrid(*nd):
    return tuple(M[i].T for i in np.meshgrid(*nd))


numel = np.size
randn = lambda shape: M[np.random.randn(*shape)]


def size(a):
    if np.size(a) == 1:
        return 1, 1
    else:
        return np.shape(a)


def rng(*args, **kwargs):
    return np.random.seed(0)


sinc, exp, linspace = (
    matlab_function_decorators()(f) for f in (np.sinc, np.exp, np.linspace)
)


@matlab_function_decorators()
def mtimes(a, b):
    return M[a] @ b


@matlab_function_decorators()
def mldivide(a, b):
    r"""Ax = B => x = A\B"""
    a, b = (
        (True, np.reshape(i, 1)[0]) if np.size(i) == 1 else (False, i) for i in (a, b)
    )
    if a[0] or b[0]:
        return M[b[1] / a[1]]
    else:
        return M[np.linalg.solve(a[1], b[1])]


@matlab_function_decorators()
def mrdivide(b, a):
    r"""xA = B => x = B/A = (A'\B')'"""
    a, b = (
        (True, np.reshape(i, 1)[0]) if np.size(i) == 1 else (False, i) for i in (a, b)
    )
    if a[0] or b[0]:
        return M[b[1] / a[1]]
    else:
        return M[np.linalg.solve(a[1].T, b[1].T).T]
