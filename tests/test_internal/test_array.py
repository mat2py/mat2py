# type: ignore
"""Tests for `MatArray`"""
import numpy as np
import pytest

import mat2py.core as mp
from mat2py.core import I, M, colon, end


def test_array():
    d1 = M[np.arange(12)]

    assert d1.shape == (1, 12)
    assert d1(1) == 0
    assert d1[0, 1] == 1
    assert d1(end) == 11
    assert d1[end - 1] == 10
    assert np.all(
        d1[I[M[[M[1:2:end], M[2:2:end]]]]]
        == [*np.arange(0, 12, 2), *np.arange(1, 12, 2)]
    )

    assert np.allclose(d1[I[2:end]], np.arange(1, 12))
    assert np.allclose(d1(I[2:end]), np.arange(1, 12))
    assert np.allclose(d1(colon(2, end)), np.arange(1, 12))

    d1 = M[1:12].T
    assert d1[I[d1 > 10]].shape == (2, 1)
    assert np.allclose(d1[I[d1 > 10]], np.array([[11], [12]]))

    d2 = M[np.copy(np.arange(12).reshape(4, 3).T)]

    assert d2.shape == (3, 4)
    assert np.allclose(d2(1), 0)
    assert np.allclose(d2[1], [1, 4, 7, 10])
    assert np.allclose(d2[I[1]], 0)
    assert np.allclose(d2(end), 11)
    assert np.allclose(d2[end - 1], 10)
    assert np.allclose(d2[I[(end - 5) : end]], np.arange(6, 12))
    assert np.allclose(d2(I[(end - 5) : end]), np.arange(6, 12))

    assert np.allclose(d2[I[2, :]], np.array([[1, 4, 7, 10]]))
    assert np.allclose(d2[I[2:3, M[2:3]]], np.array([[4, 7], [5, 8]]))
    assert np.allclose(d2[I[M[[2, 3]], M[[2, 3]]]], np.array([[4, 7], [5, 8]]))
    assert np.allclose(d2[I[M[[2, 3]]]], np.array([1, 2]))
    assert np.allclose(d2[I[M[2, 3]]], np.array([1, 2]))
    assert np.allclose(d2[I[:, 2]], np.array([3, 4, 5]))
    assert np.allclose(d2[I[:, d2.sum(0) > 20]], np.array([[6, 9], [7, 10], [8, 11]]))
    assert np.allclose(d2[I[d2 > 7]], np.array([8, 9, 10, 11]))

    assert M[1].shape == (1, 1)
    assert np.allclose(M[[]], np.array([]))
    assert np.allclose(M[1, 2], np.array([1, 2]).reshape(-1, 1))
    assert np.allclose(M[[1, 2]], np.array([1, 2]))
    assert np.allclose(M[[1, 2], [3, 4]], np.array([[1, 2], [3, 4]]))
    assert np.allclose(M[[1, 2, 3], [3, M[[4, 5]]]], np.array([[1, 2, 3], [3, 4, 5]]))
    assert np.allclose(M[1:2:12], np.arange(1, 13, 2))
    assert np.allclose(
        M[M[1:2:12], M[3:2:14]], np.vstack((np.arange(1, 13, 2), np.arange(3, 15, 2)))
    )
