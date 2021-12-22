# type: ignore
"""Tests for keyword `end`"""
import pytest

from mat2py.core import End, end


@pytest.mark.parametrize(
    ("expr", "expected"),
    [
        (None, 10),
        (-1, 9),
        (10, 0),
    ],
)
def test_end(expr, expected):
    s = 10
    if expr is not None:
        assert end(expr) == expr
        assert End(expr)(s) == s + expr
