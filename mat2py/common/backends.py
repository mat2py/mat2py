# type: ignore[attr-defined]
# This package is mainly used for numpy/scipy... compatible replacement in the future

import numpy as numpy
import scipy as scipy
from scipy import linalg as linalg

# backup important python build-in functions
py_all = all
py_any = any
py_eval = eval
py_slice = slice
py_zip = zip

try:
    # for line_profile
    from builtins import profile as py_profile
except ImportError:
    py_profile = lambda f: f
