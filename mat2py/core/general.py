# type: ignore
from types import SimpleNamespace as _SimpleNamespace

import scipy.io

from mat2py.common.backends import numpy as np

from ._internal.array import M, _convert_scalar
from ._internal.cell import cell
from ._internal.helper import argout_wrapper_decorators


def setmcruserdata(*args):
    raise NotImplementedError("setmcruserdata")


def path2rc(*args):
    raise NotImplementedError("path2rc")


def mexdebug(*args):
    raise NotImplementedError("mexdebug")


def membrane(*args):
    raise NotImplementedError("membrane")


def usejava(*args):
    raise NotImplementedError("usejava")


def recycle(*args):
    raise NotImplementedError("recycle")


def memory(*args):
    raise NotImplementedError("memory")


def matlabpath(*args):
    raise NotImplementedError("matlabpath")


def libpointer(*args):
    raise NotImplementedError("libpointer")


def inmem(*args):
    raise NotImplementedError("inmem")


def ls(*args):
    raise NotImplementedError("ls")


def mex(*args):
    raise NotImplementedError("mex")


def which(*args):
    raise NotImplementedError("which")


def saveas(*args):
    raise NotImplementedError("saveas")


def desktop(*args):
    raise NotImplementedError("desktop")


def clearvars(*args):
    raise NotImplementedError("clearvars")


def genpath(*args):
    raise NotImplementedError("genpath")


def perl(*args):
    raise NotImplementedError("perl")


def callgraphviz(*args):
    raise NotImplementedError("callgraphviz")


def depfunprophelper(*args):
    raise NotImplementedError("depfunprophelper")


def format(*args):
    raise NotImplementedError("format")


def javarmpath(*args):
    raise NotImplementedError("javarmpath")


def toolboxdir(*args):
    raise NotImplementedError("toolboxdir")


def system(*args):
    raise NotImplementedError("system")


def _import(*args):
    raise NotImplementedError("_import")


def more(*args):
    raise NotImplementedError("more")


def exit(*args):
    raise NotImplementedError("exit")


def copyfile(*args):
    raise NotImplementedError("copyfile")


def ispc(*args):
    raise NotImplementedError("ispc")


def unix(*args):
    raise NotImplementedError("unix")


def savepath(*args):
    raise NotImplementedError("savepath")


def maxNumCompThreads(*args):
    raise NotImplementedError("maxNumCompThreads")


def verLessThan(*args):
    raise NotImplementedError("verLessThan")


def getenv(*args):
    raise NotImplementedError("getenv")


def dir(*args):
    raise NotImplementedError("dir")


def ismcc(*args):
    raise NotImplementedError("ismcc")


def dos(*args):
    raise NotImplementedError("dos")


def fileattrib(*args):
    raise NotImplementedError("fileattrib")


def beep(*args):
    raise NotImplementedError("beep")


def setenv(*args):
    raise NotImplementedError("setenv")


def pack(*args):
    raise NotImplementedError("pack")


def mex_legacy(*args):
    raise NotImplementedError("mex_legacy")


def whos(*args):
    raise NotImplementedError("whos")


def what(*args):
    raise NotImplementedError("what")


def who(*args):
    raise NotImplementedError("who")


def finfo(*args):
    raise NotImplementedError("finfo")


def mkdir(*args):
    raise NotImplementedError("mkdir")


def libstruct(*args):
    raise NotImplementedError("libstruct")


def calllib(*args):
    raise NotImplementedError("calllib")


def depfun(*args):
    raise NotImplementedError("depfun")


def quit(*args):
    raise NotImplementedError("quit")


def isdir(*args):
    raise NotImplementedError("isdir")


def pwd(*args):
    raise NotImplementedError("pwd")


def clear(*args):
    pass


def type(*args):
    raise NotImplementedError("type")


def isstudent(*args):
    raise NotImplementedError("isstudent")


def path(*args):
    raise NotImplementedError("path")


def depdir(*args):
    raise NotImplementedError("depdir")


def ismac(*args):
    raise NotImplementedError("ismac")


def javaaddpath(*args):
    raise NotImplementedError("javaaddpath")


def settings(*args):
    raise NotImplementedError("settings")


def addpath(*args):
    raise NotImplementedError("addpath")


def isdeployed(*args):
    raise NotImplementedError("isdeployed")


def mex_helper(*args):
    raise NotImplementedError("mex_helper")


def movefile(*args):
    raise NotImplementedError("movefile")


def cd(*args):
    raise NotImplementedError("cd")


def syntax(*args):
    raise NotImplementedError("syntax")


def pcode(*args):
    raise NotImplementedError("pcode")


def unloadlibrary(*args):
    raise NotImplementedError("unloadlibrary")


def preferences(*args):
    raise NotImplementedError("preferences")


def ver(*args):
    raise NotImplementedError("ver")


def libisloaded(*args):
    raise NotImplementedError("libisloaded")


def delete(*args):
    raise NotImplementedError("delete")


def diary(*args):
    raise NotImplementedError("diary")


def libfunctions(*args):
    raise NotImplementedError("libfunctions")


def bench(*args):
    raise NotImplementedError("bench")


def save(*args):
    raise NotImplementedError("save")


def java(*args):
    raise NotImplementedError("java")


def libfunctionsview(*args):
    raise NotImplementedError("libfunctionsview")


def namelengthmax(*args):
    raise NotImplementedError("namelengthmax")


def load(path, *args):
    # somehow loadmat can not process complex value with option `matlab_compatible`
    def convert(obj):
        if isinstance(obj, np.ndarray):
            new_dtype = obj.dtype
            if obj.dtype == object:
                d = cell(obj.shape)
                _data = d.reshape(-1)
                for i, o in zip(range(obj.size), obj.reshape(-1)):
                    _data[i] = convert(o)
                return d

            if np.issubdtype(obj.dtype, np.integer):
                new_dtype = np.int_
            elif np.issubdtype(obj.dtype, np.floating):
                new_dtype = np.float_
            elif np.issubdtype(obj.dtype, np.complexfloating):
                new_dtype = np.complex_
            if np.dtype(new_dtype).itemsize > np.dtype(obj.dtype).itemsize:
                return _convert_scalar(M[obj.astype(new_dtype)])
            else:
                return _convert_scalar(M[obj])
        else:
            return obj

    data = scipy.io.loadmat(
        path,
        squeeze_me=False,
        struct_as_record=True,
        mat_dtype=False,
        chars_as_strings=True,
        variable_names=args if args else None,
    )

    return _SimpleNamespace(
        **{k: convert(v) for k, v in data.items() if not k.startswith("_")}
    )


def logo(*args):
    raise NotImplementedError("logo")


def isunix(*args):
    raise NotImplementedError("isunix")


def rmpath(*args):
    raise NotImplementedError("rmpath")


def rmdir(*args):
    raise NotImplementedError("rmdir")


def mexext(*args):
    raise NotImplementedError("mexext")


def computer(*args):
    raise NotImplementedError("computer")


def getmcruserdata(*args):
    raise NotImplementedError("getmcruserdata")


def rehash(*args):
    raise NotImplementedError("rehash")


def onCleanup(*args):
    raise NotImplementedError("onCleanup")


def open(*args):
    raise NotImplementedError("open")


def javaclasspath(*args):
    raise NotImplementedError("javaclasspath")


def echo(*args):
    raise NotImplementedError("echo")
