# type: ignore
"""Tests for keyword `end`"""
import numpy as np
import pytest

from mat2py.core import *


@pytest.mark.parametrize(
    ("args", "expected"),
    [
        ((1, 10), slice(0, 10, 1)),
        ((1, end), slice(0, 10, 1)),
        ((1, 2, 10), slice(0, 10, 2)),
        ((end, end / 2, end), slice(9, 10, 5)),
        ((2, end / 2.6, end - 20), slice(1, 1, 4)),
        ((1, 10), np.arange(1, 11)),
        ((1, 0.5, 10), np.arange(1, 10.1, 0.5)),
    ],
)
def test_colon(args, expected):
    length = 10
    if isinstance(expected, slice):
        assert colon(*args).to_index(length) == expected
    else:
        assert np.all(colon(*args).view(expected.dtype) == expected)


def test_colon_attr():
    seq = colon(1, 10)

    assert seq.to_index(10) == slice(0, 10, 1)
    assert seq[0, 1] == 2
    assert seq.size == 10
    assert seq.shape == (1, 10)
    assert seq.sum() == (1 + 10) * 10 / 2
    assert np.allclose(seq.to_index(10), np.arange(0, 10))
    assert np.allclose(np.array(list(iter(seq))).reshape(-1), np.arange(1, 11))
    assert next(iter(seq)) == 1
    assert seq[I[seq > 5]].shape == (1, 5)
    assert np.allclose(seq[seq > 5], np.arange(6, 11))

    seq = colon(1, 10)
    seq[:] = colon(2, 11)
    assert np.allclose(seq, np.arange(2, 12))
    assert seq.__class__.__name__ == "Colon"

    seq += colon(2, 11)
    assert np.allclose(seq, np.arange(2, 12) * 2)
    assert seq.__class__.__name__ == "MatArray"


@pytest.mark.parametrize(
    ("args", "kwargs", "dtype", "expected_type"),
    [
        (tuple(), {}, int, "MatArray"),
        ((np.ndarray,), {}, int, "ndarray"),
        ((float,), {}, float, "MatArray"),
        ((float,), {"type": np.ndarray}, float, "ndarray"),
        ((None,), {}, None, "MatArray"),
        (tuple(), {"type": np.ndarray, "dtype": None}, None, "ndarray"),
    ],
)
def test_colon_view(args, kwargs, dtype, expected_type):
    seq = colon(1, 10)
    view = seq.view(*args, **kwargs)
    value = np.arange(1, 11).view(dtype)

    assert np.all(view == value)
    assert view.__class__.__name__ == expected_type
