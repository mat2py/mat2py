# type: ignore
import pytest

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


def test_ismember():
    A = reshape(M[[5, 3, 4, 2]], 2, M[[]])
    B = reshape(M[[2, 4, 4, 4, 6, 8]], M[[]], 2)

    Lia = ismember(A, B)
    assert_same_array(
        Lia,
        M[
            [0, 1],
            [0, 1],
        ],
        ignore_bool=True,
    )

    Lia, Locb = ismember(A, B)

    assert_same_array(
        Lia,
        M[
            [0, 1],
            [0, 1],
        ],
        ignore_bool=True,
    )

    assert_same_array(
        Locb,
        M[
            [0, 2],
            [0, 1],
        ],
    )


def test_times():
    a = M[[1, 2]]

    # TODO: this should raise dimension mismatch error in matlab
    a.H * a


def test_any():
    from mat2py.core.ops import _any

    A = M[
        [0, 1, 2],
        [2, 3, 4],
        [0, 4, 2],
        [4, 2, 6],
    ]

    assert_same_array(
        _any(A),
        M[[1, 1, 1]],
        ignore_bool=True,
    )
    assert_same_array(
        _any(A == 1),
        M[[0, 1, 0]],
        ignore_bool=True,
    )
    assert_same_array(
        _any(A, "all"),
        M[[1]],
        ignore_bool=True,
    )
    assert_same_array(
        _any(A == 3, 2),
        M[
            0,
            1,
            0,
            0,
        ],
        ignore_bool=True,
    )
