# type: ignore
import pytest

from mat2py.core import *

from .helper import *


def test_sort():
    assert_same_array(
        sort(M[[9, 0, -7, 5, 3, 8, -10, 4, 2]]), M[[-10, -7, 0, 2, 3, 4, 5, 8, 9]]
    )
    assert_same_array(
        sort(M[9, 0, -7, 5, 3, 8, -10, 4, 2]), M[-10, -7, 0, 2, 3, 4, 5, 8, 9]
    )
    assert_same_array(
        sort(
            M[
                [3, 6, 5],
                [7, -2, 4],
                [1, 0, -9],
            ]
        ),
        M[
            [1, -2, -9],
            [3, 0, 4],
            [7, 6, 5],
        ],
    )


def test_sum():
    A = M[
        [1, 3, 2],
        [4, 2, 5],
        [6, 1, 4],
    ]
    assert_same_array(sum(M[1:10]), M[[55]])
    assert_same_array(sum(A), M[[11, 6, 11]])
    assert_same_array(sum(A, 2), M[6, 11, 11])
    assert_same_array(sum(ones(4, 2, 3), 3), ones(4, 2) * 3)
