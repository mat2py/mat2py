# type: ignore
__all__ = ["sinc", "py_sinc"]

import mat2py as mp
from mat2py.common.backends import numpy as np
from mat2py.core import *
from mat2py.core._internal.helper import (
    mp_argout_wrapper_decorators,
    mp_pass_values_decorators,
)


@mp_pass_values_decorators()
# Automatically converted from Matlab code
def sinc(x):
    i = find(x == 0)
    x[I[i]] = 1
    y = sin(pi @ M[x]) / (pi @ M[x])
    y[I[i]] = 1
    return y


py_sinc = mp_argout_wrapper_decorators()(np.sinc)
