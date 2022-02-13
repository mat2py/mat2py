# type: ignore
from ._internal.array import M
from ._internal.helper import matlab_function_decorators
from ._internal.package_proxy import numpy as np

# sinc belongs to the signal package but for now lets put it here
(sinc, exp, real, imag, angle, conj) = (
    matlab_function_decorators()(f)
    for f in (
        np.sinc,
        np.exp,
        np.real,
        np.imag,
        np.angle,
        np.conj,
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


def imag(*args):
    raise NotImplementedError("imag")


def log10(*args):
    raise NotImplementedError("log10")


def asecd(*args):
    raise NotImplementedError("asecd")


def cscd(*args):
    raise NotImplementedError("cscd")


def acotd(*args):
    raise NotImplementedError("acotd")


def sinh(*args):
    raise NotImplementedError("sinh")


def sin(*args):
    raise NotImplementedError("sin")


def mod(*args):
    raise NotImplementedError("mod")


def cos(*args):
    raise NotImplementedError("cos")


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


def floor(*args):
    raise NotImplementedError("floor")


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


def sqrt(*args):
    raise NotImplementedError("sqrt")


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


def tanh(*args):
    raise NotImplementedError("tanh")


def csc(*args):
    raise NotImplementedError("csc")


def cosh(*args):
    raise NotImplementedError("cosh")


def abs(*args):
    raise NotImplementedError("abs")


def ceil(*args):
    raise NotImplementedError("ceil")


def acot(*args):
    raise NotImplementedError("acot")


def real(*args):
    raise NotImplementedError("real")


def nextpow2(*args):
    raise NotImplementedError("nextpow2")


def tan(*args):
    raise NotImplementedError("tan")


def realpow(*args):
    raise NotImplementedError("realpow")


def asinh(*args):
    raise NotImplementedError("asinh")
