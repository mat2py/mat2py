# type: ignore
"""Tests for keyword `end`"""
import numpy as np
import pytest

from mat2py.core import *


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
        ((-((end**2 + 11) - 9) / 2) * (+(11 + end)) // 8 % 7, 10, 6),
        (((end - 6.0000000000000001) / 3) * 6, 10, 8),  # Matlab does round
    ],
)
def test_end(expr, size, expected):
    assert expr(size) == expected
