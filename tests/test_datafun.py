# type: ignore
import pytest

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
    assert_same_array(sum(A, "all"), M[28])
    assert_same_array(sum(A, 2), M[6, 11, 11])
    assert_same_array(sum(ones(4, 2, 3), 3), ones(4, 2) * 3)


def test_trapz():
    Y = M[[1, 4, 9, 16, 25]]
    Q = trapz(Y)
    assert_same_array(Q, M[42.0])

    X = M[0 : (pi / 100) : pi]
    Y = sin(X)
    Q = trapz(X, Y)
    assert_same_array(Q, M[1.9998], close=True, atol=1.0e-4)

    X = (M[[1, 2.5, 7, 10]]).H
    Y = M[
        [5.2, 4.8, 4.9, 5.1],
        [7.7, 7.0, 6.5, 6.8],
        [9.6, 10.5, 10.5, 9.0],
        [13.2, 14.5, 13.8, 15.2],
    ]
    Q = trapz(X, Y)
    assert_same_array(Q, M[[82.8000, 85.7250, 83.2500, 80.7750]], close=True)

    x = M[(-3):0.1:3]
    y = M[(-5):0.1:5]
    X, Y = meshgrid(x, y)
    F = (X**2) + (Y**2)
    _I = trapz(y, trapz(x, F, 2))
    assert_same_array(_I, M[680.2000], close=True)
