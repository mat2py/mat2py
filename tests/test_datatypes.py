# type: ignore
import pytest

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


def test_struct():
    S1 = struct("a", "Sausage", "b", M[[1, 5, 0.15]])

    s = struct()
    s.a = "Sausage"
    s.b = M[[1, 5, 0.15]]

    assert s.a == S1["a"]
    assert_same_array(s.b, S1.b)
