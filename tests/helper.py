# type: ignore
import pytest

from mat2py.core import *


def assert_same_array(a, b):
    assert a.shape == b.shape
    assert a.dtype == b.dtype
    assert np.all(a == b)
