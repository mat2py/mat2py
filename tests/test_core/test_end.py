# type: ignore
"""Tests for keyword `end`"""
import numpy as np
import pytest

from mat2py.core import colon, end


@pytest.mark.parametrize(
    ("expr", "size", "expected"),
    [
        (end, 10, 10),
        (end, 20, 20),
        (end - 1, 10, 9),
        (-9 + end, 10, 1),
        (end - 9, 10, 1),
        (end - 10, 10, 0),
        (end - 11, 10, -1),
        (-(5 - end), 10, 5),
        (end % 7, 10, 3),
        (end // 6, 10, 1),
        (end / 2, 10, 5),
        ((-((end ** 2 + 11) - 9) / 2) * (+(11 + end)) // 8 % 7, 10, 6),
        (((end - 6.0000000000000001) / 3) * 6, 10, 8),  # Matlab does round
    ],
)
def test_end(expr, size, expected):
    assert expr(size) == expected


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
    assert seq[1] == 2
    assert seq.size == 10
    assert seq.shape == (10,)
    assert seq.sum() == (1 + 10) * 10 / 2
    assert np.allclose(seq.to_index(10), np.arange(0, 10))
    assert np.allclose(list(iter(seq)), np.arange(1, 11))

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
