# type: ignore
import pytest

from mat2py.core import *

from .helper import *


def test_floor():
    X = M[
        [-1.9, -0.2, 3.4],
        [5.6, 7.0, 2.4 + 3.6j],
    ]
    Y = floor(X)
    assert_same_array(
        Y,
        M[
            [(-2.0000) + 0.0000j, (-1.0000) + 0.0000j, 3.0000 + 0.0000j],
            [5.0000 + 0.0000j, 7.0000 + 0.0000j, 2.0000 + 3.0000j],
        ],
    )
    # TODO: we will support time type later
    # t = (hours(8) + minutes(M[29:31])) + seconds(1.23)
    # t.Format = 'hh:mm:ss.SS'
    # _assert(t == (M[[M[08:29:01.23], M[08:30:01.23], M[08:31:01.23]]]))
    # Y1 = floor(t)
    # _assert(t == (M[[M[08:29:01.00], M[08:30:01.00], M[08:31:01.00]]]))
    # Y2 = floor(t, 'hours')
    # _assert(t == (M[[M[08:00:00.00], M[08:00:00.00], M[08:00:00.00]]]))

    # floor as index
    assert_same_array(X(1, floor(3.99)), 3.4 + 0j)

    # floor as loop
    for y4 in M[1 : floor(3.1)]:
        pass

    assert_same_array(y4, 3.0)
