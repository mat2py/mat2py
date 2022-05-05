# type: ignore
__all__ = [
    "randperm",
    "rand",
    "randn",
    "rng",
    "randi",
]

from mat2py.common.backends import numpy as np

from ._internal.helper import argout_wrapper_decorators
from ._internal.math_helper import _rand_like_decorators


def randperm(*args):
    raise NotImplementedError("randperm")


rand = _rand_like_decorators()(np.random.rand)
randn = _rand_like_decorators()(np.random.randn)


def rng(*args):
    return np.random.seed(0)


def randi(*args):
    raise NotImplementedError("randi")
