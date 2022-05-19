# type: ignore
__all__ = [
    "regexptranslate",
    "dec2bin",
    "strrep",
    "strtok",
    "hex2dec",
    "strings",
    "base2dec",
    "strmatch",
    "char",
    "strread",
    "native2unicode",
    "strcat",
    "blanks",
    "strvcat",
    "strjoin",
    "hex2num",
    "unicode2native",
    "strsplit",
    "dec2hex",
    "str2double",
    "iscellstr",
    "sprintf",
    "regexp",
    "strcmpi",
    "upper",
    "strfind",
    "strncmp",
    "sscanf",
    "str2mat",
    "strcmp",
    "dec2base",
    "num2hex",
    "isletter",
    "ischar",
    "strtrim",
    "setstr",
    "mat2str",
    "isstr",
    "cellstr",
    "deblank",
    "strjust",
    "isstrprop",
    "regexprep",
    "findstr",
    "int2str",
    "regexpi",
    "isspace",
    "str2num",
    "strncmpi",
    "num2str",
    "bin2dec",
    "lower",
]

from mat2py.common.backends import numpy as np

from ._internal.array import M, mp_convert_scalar, mp_detect_vector


def regexptranslate(*args):
    raise NotImplementedError("regexptranslate")


def dec2bin(*args):
    raise NotImplementedError("dec2bin")


def strrep(*args):
    raise NotImplementedError("strrep")


def strtok(*args):
    raise NotImplementedError("strtok")


def hex2dec(*args):
    raise NotImplementedError("hex2dec")


def strings(*args):
    raise NotImplementedError("strings")


def base2dec(*args):
    raise NotImplementedError("base2dec")


def strmatch(*args):
    raise NotImplementedError("strmatch")


def char(*args):
    raise NotImplementedError("char")


def strread(*args):
    raise NotImplementedError("strread")


def native2unicode(*args):
    raise NotImplementedError("native2unicode")


def strcat(*args):
    if all(isinstance(arg, str) for arg in args):
        return "".join(args).rstrip()
    raise NotImplementedError("strcat")


def blanks(*args):
    raise NotImplementedError("blanks")


def strvcat(*args):
    raise NotImplementedError("strvcat")


def strjoin(*args):
    raise NotImplementedError("strjoin")


def hex2num(*args):
    raise NotImplementedError("hex2num")


def unicode2native(*args):
    raise NotImplementedError("unicode2native")


def strsplit(*args):
    raise NotImplementedError("strsplit")


def dec2hex(*args):
    raise NotImplementedError("dec2hex")


def str2double(*args):
    raise NotImplementedError("str2double")


def iscellstr(*args):
    raise NotImplementedError("iscellstr")


def sprintf(*args):
    raise NotImplementedError("sprintf")


def regexp(*args):
    raise NotImplementedError("regexp")


def strcmpi(*args):
    raise NotImplementedError("strcmpi")


def upper(*args):
    raise NotImplementedError("upper")


def strfind(*args):
    raise NotImplementedError("strfind")


def strncmp(*args):
    raise NotImplementedError("strncmp")


def sscanf(*args):
    raise NotImplementedError("sscanf")


def str2mat(*args):
    raise NotImplementedError("str2mat")


def strcmp(*args):
    raise NotImplementedError("strcmp")


def dec2base(*args):
    raise NotImplementedError("dec2base")


def num2hex(*args):
    raise NotImplementedError("num2hex")


def isletter(*args):
    raise NotImplementedError("isletter")


def ischar(*args):
    raise NotImplementedError("ischar")


def strtrim(*args):
    raise NotImplementedError("strtrim")


def setstr(*args):
    raise NotImplementedError("setstr")


def mat2str(*args):
    raise NotImplementedError("mat2str")


def isstr(*args):
    raise NotImplementedError("isstr")


def cellstr(*args):
    raise NotImplementedError("cellstr")


def deblank(*args):
    raise NotImplementedError("deblank")


def strjust(*args):
    raise NotImplementedError("strjust")


def isstrprop(*args):
    raise NotImplementedError("isstrprop")


def regexprep(*args):
    raise NotImplementedError("regexprep")


def findstr(*args):
    raise NotImplementedError("findstr")


def int2str(*args):
    raise NotImplementedError("int2str")


def regexpi(*args):
    raise NotImplementedError("regexpi")


def isspace(*args):
    raise NotImplementedError("isspace")


def str2num(*args):
    raise NotImplementedError("str2num")


def strncmpi(*args):
    raise NotImplementedError("strncmpi")


def num2str(a, *args):
    if args:
        raise NotImplementedError("num2str")
    s = M[a]
    assert np.issubdtype(s.dtype, np.number)
    if np.size(s) == 1:
        return str(mp_convert_scalar(a))

    # TODO: not compatible with Matlab, we need character array
    s = s.astype(str).view(np.ndarray)

    if mp_detect_vector(s) == 1:
        return " ".join(s.reshape(-1))

    max_length = np.apply_along_axis(lambda c: max(len(i) for i in c), 0, s)
    s = np.apply_along_axis(
        lambda r: " ".join(s.rjust(l, " ") for s, l in zip(r, max_length)), 1, s
    )

    return M[s].reshape(-1, 1)


def bin2dec(*args):
    raise NotImplementedError("bin2dec")


def lower(*args):
    raise NotImplementedError("lower")
