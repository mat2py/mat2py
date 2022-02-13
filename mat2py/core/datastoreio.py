# type: ignore
from ._internal.array import M
from ._internal.helper import matlab_function_decorators
from ._internal.package_proxy import numpy as np


def readDatastoreImage(*args):
    raise NotImplementedError("readDatastoreImage")


def datastore(*args):
    raise NotImplementedError("datastore")
