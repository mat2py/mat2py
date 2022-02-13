# type: ignore
from ._internal.array import M
from ._internal.helper import matlab_function_decorators
from ._internal.package_proxy import numpy as np


def mapreduce(*args):
    raise NotImplementedError("mapreduce")


def mapreducer(*args):
    raise NotImplementedError("mapreducer")


def gcmr(*args):
    raise NotImplementedError("gcmr")
