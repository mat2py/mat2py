# type: ignore
from ._internal.array import M
from ._internal.helper import argout_wrapper_decorators
from ._internal.package_proxy import numpy as np


def hdsGetSize(*args):
    raise NotImplementedError("hdsGetSize")


def hdsCatArray(*args):
    raise NotImplementedError("hdsCatArray")


def hdsNewArray(*args):
    raise NotImplementedError("hdsNewArray")


def hdsReplicateArray(*args):
    raise NotImplementedError("hdsReplicateArray")


def hdsGetSlice(*args):
    raise NotImplementedError("hdsGetSlice")


def hdsReshapeArray(*args):
    raise NotImplementedError("hdsReshapeArray")


def hdsSetSlice(*args):
    raise NotImplementedError("hdsSetSlice")
