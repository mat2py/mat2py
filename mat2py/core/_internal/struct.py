# type: ignore

from types import SimpleNamespace

from mat2py.common.backends import numpy as np

from .array import M, MatArray, _convert_round, _convert_scalar, _convert_to_2d
from .cell import C, CellArray


class Struct(SimpleNamespace):
    def __getitem__(self, item):
        return getattr(self, item)


class StructArray(Struct):
    # TODO: we should implement StructArray
    pass


def _fieldnames(a):
    assert isinstance(a, StructArray)
    return [i for i in a.__dict__.keys() if not i.startswith("__")]


def fieldnames(a, *args):
    if args:
        raise NotImplementedError("fieldnames")
    return C.__class_getitem__(*_fieldnames(a))


def struct(*args):
    if len(args) == 0:
        return StructArray()
    if len(args) == 1:
        raise NotImplementedError
    assert len(args) % 2 == 0
    names, values = args[::2], args[1::2]
    assert all(isinstance(i, str) for i in names)

    if any(isinstance(i, CellArray) for i in values):
        raise NotImplementedError

    return StructArray(**dict(zip(names, values)))
