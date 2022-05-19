# type: ignore
import pytest

from .helper import *


def test_num2str():
    assert num2str(3.14) == "3.14"
    assert num2str(M[[1, 2, 3]]) == "1 2 3"
    assert all(num2str(M[[1, 2, 3], [9, 10, 11]]) == M["1  2  3", "9 10 11"])
