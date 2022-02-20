# type: ignore
from time import time as _time

from mat2py.common.backends import numpy as np

from ._internal.array import M
from ._internal.helper import argout_wrapper_decorators


def timezones(*args):
    raise NotImplementedError("timezones")


def weekday(*args):
    raise NotImplementedError("weekday")


def caldays(*args):
    raise NotImplementedError("caldays")


def etime(*args):
    raise NotImplementedError("etime")


def timeit(*args):
    raise NotImplementedError("timeit")


def cputime(*args):
    raise NotImplementedError("cputime")


def isdatetime(*args):
    raise NotImplementedError("isdatetime")


def datenum(*args):
    raise NotImplementedError("datenum")


def eomday(*args):
    raise NotImplementedError("eomday")


def tic(nargout=0):
    if nargout != 0:
        raise NotImplementedError("tic")
    tic.timerVal = _time()
    return tic.timerVal


def toc(*args, nargout=1):
    interval = _time() - (args[0] if args else tic.timerVal)
    if nargout == 0:
        print(f"Elapsed time is {interval:10.5g} seconds.")
    return interval


def days(*args):
    raise NotImplementedError("days")


def datevec(*args):
    raise NotImplementedError("datevec")


def iscalendarduration(*args):
    raise NotImplementedError("iscalendarduration")


def isduration(*args):
    raise NotImplementedError("isduration")


def clock(*args):
    raise NotImplementedError("clock")


def calyears(*args):
    raise NotImplementedError("calyears")


def milliseconds(*args):
    raise NotImplementedError("milliseconds")


def minutes(*args):
    raise NotImplementedError("minutes")


def hours(*args):
    raise NotImplementedError("hours")


def addtodate(*args):
    raise NotImplementedError("addtodate")


def seconds(*args):
    raise NotImplementedError("seconds")


def calweeks(*args):
    raise NotImplementedError("calweeks")


def NaT(*args):
    raise NotImplementedError("NaT")


def datestr(*args):
    raise NotImplementedError("datestr")


def calquarters(*args):
    raise NotImplementedError("calquarters")


def datetick(*args):
    raise NotImplementedError("datetick")


def now(*args):
    raise NotImplementedError("now")


def date(*args):
    raise NotImplementedError("date")


def calmonths(*args):
    raise NotImplementedError("calmonths")


def pause(*args):
    raise NotImplementedError("pause")


def calendar(*args):
    raise NotImplementedError("calendar")


def years(*args):
    raise NotImplementedError("years")
