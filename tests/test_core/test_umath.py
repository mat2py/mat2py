# type: ignore
import pytest

from mat2py.core import *


def test_mrdivide():
    Wn = mrdivide((colon(0, 3)).T, 8)
    assert Wn.shape == (4, 1)
