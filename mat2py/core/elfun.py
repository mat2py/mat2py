# type: ignore
from mat2py.common.backends import numpy as np

from ._internal.array import M
from ._internal.helper import argout_wrapper_decorators

(exp, real, imag, abs, angle, conj, sin, cos, sinh, cosh, tan, tanh, sqrt) = (
    argout_wrapper_decorators()(f)
    for f in (
        np.exp,
        np.real,
        np.imag,
        np.abs,
        np.angle,
        np.conj,
        np.sin,
        np.cos,
        np.sinh,
        np.cosh,
        np.tan,
        np.tanh,
        np.sqrt,
    )
)


def log(*args):
    raise NotImplementedError("log")


def sech(*args):
    raise NotImplementedError("sech")


def atan(*args):
    raise NotImplementedError("atan")


def cot(*args):
    raise NotImplementedError("cot")


def coth(*args):
    raise NotImplementedError("coth")


def acsch(*args):
    raise NotImplementedError("acsch")


def acsc(*args):
    raise NotImplementedError("acsc")


def log10(*args):
    raise NotImplementedError("log10")


def asecd(*args):
    raise NotImplementedError("asecd")


def cscd(*args):
    raise NotImplementedError("cscd")


def acotd(*args):
    raise NotImplementedError("acotd")


def mod(*args):
    raise NotImplementedError("mod")


def acosh(*args):
    raise NotImplementedError("acosh")


def atanh(*args):
    raise NotImplementedError("atanh")


def atan2(*args):
    raise NotImplementedError("atan2")


def fix(*args):
    raise NotImplementedError("fix")


def asind(*args):
    raise NotImplementedError("asind")


def asec(*args):
    raise NotImplementedError("asec")


def complex(*args):
    raise NotImplementedError("complex")


def floor(x, *args):
    if args:
        raise NotImplementedError("floor")
    else:
        return M[np.floor(x)]


def nthroot(*args):
    raise NotImplementedError("nthroot")


def cosd(*args):
    raise NotImplementedError("cosd")


def atan2d(*args):
    raise NotImplementedError("atan2d")


def tand(*args):
    raise NotImplementedError("tand")


def sign(*args):
    raise NotImplementedError("sign")


def isreal(*args):
    raise NotImplementedError("isreal")


def reallog(*args):
    raise NotImplementedError("reallog")


def rem(*args):
    raise NotImplementedError("rem")


def cotd(*args):
    raise NotImplementedError("cotd")


def deg2rad(*args):
    raise NotImplementedError("deg2rad")


def acscd(*args):
    raise NotImplementedError("acscd")


def secd(*args):
    raise NotImplementedError("secd")


def pow2(*args):
    raise NotImplementedError("pow2")


def sec(*args):
    raise NotImplementedError("sec")


def csch(*args):
    raise NotImplementedError("csch")


def acos(*args):
    raise NotImplementedError("acos")


def unwrap(*args):
    raise NotImplementedError("unwrap")


def rad2deg(*args):
    raise NotImplementedError("rad2deg")


def acoth(*args):
    raise NotImplementedError("acoth")


def log2(*args):
    raise NotImplementedError("log2")


def log1p(*args):
    raise NotImplementedError("log1p")


def asech(*args):
    raise NotImplementedError("asech")


def asin(*args):
    raise NotImplementedError("asin")


def realsqrt(*args):
    raise NotImplementedError("realsqrt")


def hypot(*args):
    raise NotImplementedError("hypot")


def expm1(*args):
    raise NotImplementedError("expm1")


def atand(*args):
    raise NotImplementedError("atand")


def acosd(*args):
    raise NotImplementedError("acosd")


def cplxpair(*args):
    raise NotImplementedError("cplxpair")


def round(*args):
    raise NotImplementedError("round")


def sind(*args):
    raise NotImplementedError("sind")


def csc(*args):
    raise NotImplementedError("csc")


def ceil(x, unit=None):
    if unit is not None:
        raise NotImplementedError("ceil")
    else:
        return M[np.ceil(x)]


def acot(*args):
    raise NotImplementedError("acot")


def nextpow2(*args):
    raise NotImplementedError("nextpow2")


def realpow(*args):
    raise NotImplementedError("realpow")


def asinh(*args):
    raise NotImplementedError("asinh")
