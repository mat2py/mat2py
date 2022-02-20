# type: ignore
from mat2py.common.backends import numpy as np

from ._internal.array import I, M, end
from ._internal.cell import C
from ._internal.helper import argout_wrapper_decorators, special_variables


def copy(x):
    # ToDo: we should do copy-on-write
    return x


def doclink(*args):
    raise NotImplementedError("doclink")


def _eval(*args):
    raise NotImplementedError("eval")


def online_concatenator(*args):
    raise NotImplementedError("online_concatenator")


def display(*args):
    raise NotImplementedError("display")


def munlock(*args):
    raise NotImplementedError("munlock")


def warning(*args):
    raise NotImplementedError("warning")


def localfunctions(*args):
    raise NotImplementedError("localfunctions")


def nargin(*args):
    raise NotImplementedError("nargin")


def assignin(*args):
    raise NotImplementedError("assignin")


def genvarname(*args):
    raise NotImplementedError("genvarname")


def precedence(*args):
    raise NotImplementedError("precedence")


def handle(*args):
    raise NotImplementedError("handle")


def keyboard(*args):
    raise NotImplementedError("keyboard")


def spmd_feval(*args):
    raise NotImplementedError("spmd_feval")


def lastwarn(*args):
    raise NotImplementedError("lastwarn")


def isvarname(*args):
    raise NotImplementedError("isvarname")


def inputname(*args):
    raise NotImplementedError("inputname")


def iskeyword(*args):
    raise NotImplementedError("iskeyword")


def run(*args):
    raise NotImplementedError("run")


def reverse_binary_operator(*args):
    raise NotImplementedError("reverse_binary_operator")


def javachk(*args):
    raise NotImplementedError("javachk")


def nargout(*args):
    raise NotImplementedError("nargout")


def parfor_range_check(*args):
    raise NotImplementedError("parfor_range_check")


def details(*args):
    raise NotImplementedError("details")


ans = special_variables(None)


def validateattributes(*args):
    raise NotImplementedError("validateattributes")


def _assert(*args):
    raise NotImplementedError("_assert")


def disp(*args):
    print(*args)


def varargout(*args):
    raise NotImplementedError("varargout")


def parallel_function(*args):
    raise NotImplementedError("parallel_function")


def input(*args):
    raise NotImplementedError("input")


def isglobal(*args):
    raise NotImplementedError("isglobal")


def evalin(*args):
    raise NotImplementedError("evalin")


def mlock(*args):
    raise NotImplementedError("mlock")


def error(*args):
    print(*args)


def rethrow(*args):
    raise NotImplementedError("rethrow")


def validatestring(*args):
    raise NotImplementedError("validatestring")


def parfor_sliced_fcnhdl_check(*args):
    raise NotImplementedError("parfor_sliced_fcnhdl_check")


def exist(*args):
    raise NotImplementedError("exist")


def ParallelException(*args):
    raise NotImplementedError("ParallelException")


def checkSyntacticWarnings(*args):
    raise NotImplementedError("checkSyntacticWarnings")


def parfor_endpoint_check(*args):
    raise NotImplementedError("parfor_endpoint_check")


def builtin(*args):
    raise NotImplementedError("builtin")


def consume_assign(*args):
    raise NotImplementedError("consume_assign")


def evalc(*args):
    raise NotImplementedError("evalc")


def lasterr(*args):
    raise NotImplementedError("lasterr")


def varargin(*args):
    raise NotImplementedError("varargin")


def script(*args):
    raise NotImplementedError("script")


def nargchk(*args):
    raise NotImplementedError("nargchk")


def nargoutchk(*args):
    raise NotImplementedError("nargoutchk")


def feval(*args):
    raise NotImplementedError("feval")


def narginchk(*args):
    raise NotImplementedError("narginchk")


def lasterror(*args):
    raise NotImplementedError("lasterror")


def mislocked(*args):
    raise NotImplementedError("mislocked")


def mfilename(*args):
    raise NotImplementedError("mfilename")


def message(*args):
    raise NotImplementedError("message")


def parfor_M_check(*args):
    raise NotImplementedError("parfor_M_check")


def lists(*args):
    raise NotImplementedError("lists")
