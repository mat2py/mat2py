# type: ignore
import pytest

from mat2py.core import *


def assert_same_array(a, b, ignore_bool=False):
    assert a.shape == b.shape
    assert a.dtype == b.dtype or ignore_bool
    assert np.all(a == b)
