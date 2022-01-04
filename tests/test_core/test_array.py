# type: ignore
"""Tests for `MatArray`"""
import numpy as np
import pytest

import mat2py.core as mp
from mat2py.core import I, colon, end


def test_array():
    d1 = mp.array(np.arange(12))

    assert d1.shape == (12,)
    assert d1(1) == 0
    assert d1[1] == 1
    assert d1(end) == 11
    assert d1[end - 1] == 10

    assert np.allclose(d1[I[2:end]], np.arange(1, 12))
    assert np.allclose(d1(I[2:end]), np.arange(1, 12))
    assert np.allclose(d1(colon(2, end)), np.arange(1, 12))

    d2 = mp.array(np.copy(np.arange(12).reshape(4, 3).T))

    assert d2.shape == (3, 4)
    assert np.allclose(d2(1), 0)
    assert np.allclose(d2[1], [1, 4, 7, 10])
    assert np.allclose(d2[I[1]], 0)
    assert np.allclose(d2(end), 11)
    assert np.allclose(d2[end - 1], 10)
    assert np.allclose(d2[I[(end - 5) : end]], np.arange(6, 12))
    assert np.allclose(d2(I[(end - 5) : end]), np.arange(6, 12))

    assert np.allclose(d2[I[2, :]], np.array([[1, 4, 7, 10]]))
    assert np.allclose(d2[I[2:3, 2:3]], np.array([[4, 7], [5, 8]]))
    assert np.allclose(
        d2[I[:, 2]], np.array([3, 4, 5])
    )  # TODO: do we need to take care of row/column vector?