# type: ignore
__all__ = [
    "randperm",
    "rand",
    "randn",
    "rng",
    "randi",
]

from mat2py.common.backends import numpy as np

from ._internal.helper import mp_argout_wrapper_decorators
from ._internal.math_helper import mp_rand_like_decorators


def randperm(*args):
    raise NotImplementedError("randperm")


rand = mp_rand_like_decorators()(np.random.rand)
randn = mp_rand_like_decorators()(np.random.randn)


def rng(*args):
    return np.random.seed(0)


def randi(*args):
    raise NotImplementedError("randi")
