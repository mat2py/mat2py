# type: ignore
import pytest

from mat2py.core import *

from .helper import *


def test_find():
    x = reshape(M[-1, 0, 1, 2, -2, 5], 2, 3)
    assert_same_array(
        x,
        M[
            [-1, 1, -2],
            [0, 2, 5],
        ],
    )
    assert_same_array(
        find(x),
        M[
            1,
            3,
            4,
            5,
            6,
        ],
    )
    r = zeros(5, 1, "like", 1)
    r[I[:]], c = find(x)
    assert_same_array(r, M[1, 1, 2, 1, 2])
    assert_same_array(c, M[1, 2, 2, 3, 3])


def test_zeros():
    assert_same_array(size(ones(5, 0)), M[[5, 0]])
    assert_same_array(zeros(4), np.zeros((4, 4)))
    assert_same_array(zeros(2, 3, 4), np.zeros((2, 3, 4)))
    assert_same_array(zeros(M[[3, 2]]), np.zeros((3, 2)))
    assert_same_array(zeros(1, 3, "uint16"), np.zeros((1, 3), np.uint16))
    assert_same_array(zeros("like", M[1 + 2j, 3j]), np.zeros((1, 1), np.complex128))
    assert_same_array(zeros(M[1, 3], "like", 5.0), np.zeros((1, 3), float))


def test_isempty():
    assert_same_array(isempty(ones(5, 0)), M[1])
