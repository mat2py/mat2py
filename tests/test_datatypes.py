# type: ignore
import pytest

from mat2py.core import *

from .helper import *


def test_cell():
    c = cell(3)
    assert c.shape == (3, 3)
    for i in M[1:9]:
        assert_same_array(c[I[i]], M[[]])
    c[I[1]] = "hello"
    assert c[I[1]] == "hello"
    c[I[2:3]] = C["world", M[1:2]]
    assert c[I[2]] == "world"
    assert_same_array(c[I[3, 1]], M[1:2])
    for i in M[4:9]:
        assert_same_array(c[I[i]], M[[]])
    c[I[2:3, 2:3]] = C[[1, 2], [3, 4]]
