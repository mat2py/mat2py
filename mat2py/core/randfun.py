# type: ignore
from mat2py.common.backends import numpy as np

from ._internal.helper import argout_wrapper_decorators


def randperm(*args):
    raise NotImplementedError("randperm")


def rand(*args):
    raise NotImplementedError("rand")


@argout_wrapper_decorators()
def randn(*args):
    if len(args) == 1:
        (args,) = args
    args = args if isinstance(args, tuple) else (args,)
    return np.random.randn(*args)


def rng(*args):
    return np.random.seed(0)


def randi(*args):
    raise NotImplementedError("randi")
