# type: ignore
__all__ = ["linspace", "py_linspace"]


from mat2py.core import *
from mat2py.core._internal.helper import mp_inference_nargin_decorators

py_linspace = linspace


@mp_inference_nargin_decorators()
def linspace(d1=None, d2=None, n=None, nargin=None):
    if nargin == 2:
        n = 100
    else:
        n = floor(double(n))
    n1 = n - 1
    c = (d2 - d1) * (n1 - 1)
    if isinf(c):
        if isinf(d2 - d1):
            y = (d1 + ((mrdivide(d2, n1)) * (M[0:n1]))) - (
                (mrdivide(d1, n1)) * (M[0:n1])
            )
        else:
            y = d1 + ((M[0:n1]) * (mrdivide(d2 - d1, n1)))
    else:
        y = d1 + (mrdivide((M[0:n1]) * (d2 - d1), n1))
    if _not(isempty(y)):
        y[I[1]] = copy(d1)
        y[I[end]] = copy(d2)
    return y
