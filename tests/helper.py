# type: ignore
import pytest

from mat2py import core as _core

__all__ = [
    *_core.__all__,
    "np",
    "assert_same_array",
]

from mat2py.common.backends import numpy as np
from mat2py.core import *


def assert_same_array(a, b, ignore_bool=False, close=False, **kwargs):
    a, b = M[a], M[b]
    assert a.shape == b.shape
    assert a.dtype == b.dtype or ignore_bool
    if close:
        assert np.allclose(a, b, **kwargs)
    else:
        assert np.all(a == b)
