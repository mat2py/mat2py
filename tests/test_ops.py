# type: ignore
import pytest

from mat2py.core import *

from .helper import *


def test_unique():
    a = M[[9, 2, 9, 5]]
    c, ia, ic = unique(a)
    assert_same_array(c, M[[2, 5, 9]])
    assert_same_array(ia, M[2, 4, 1])
    assert_same_array(ic, M[3, 1, 3, 2])

    c, ia, ic = unique(reshape(a, 2, 2))
    assert_same_array(c, M[2, 5, 9])
    assert_same_array(ia, M[2, 4, 1])
    assert_same_array(ic, M[3, 1, 3, 2])


def test_mrdivide():
    Wn = mrdivide((colon(0, 3)).T, 8)
    assert Wn.shape == (4, 1)
