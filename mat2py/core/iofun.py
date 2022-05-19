# type: ignore

__all__ = [
    "home",
    "partialpath",
    "filemarker",
    "xlsread",
    "fscanf",
    "tempdir",
    "clc",
    "csvread",
    "xslt",
    "dataread",
    "unzip",
    "fileparts",
    "mltimerpackage",
    "createClassFromWsdl",
    "fopen",
    "zip",
    "fseek",
    "prefdir",
    "sendmail",
    "dlmwrite",
    "matfile",
    "urlwrite",
    "callSoapService",
    "timerfindall",
    "createSoapMessage",
    "xmlwrite",
    "dlmread",
    "fprintf",
    "importdata",
    "readtable",
    "fileread",
    "fgetl",
    "pathsep",
    "xlswrite",
    "gzip",
    "feof",
    "ferror",
    "tempname",
    "daqread",
    "xmlread",
    "fullfile",
    "fread",
    "frewind",
    "gunzip",
    "urlread",
    "instrfind",
    "matfinfo",
    "tar",
    "fileExchangeDesktopTool",
    "instrfindall",
    "csvwrite",
    "filesep",
    "writetable",
    "timerfind",
    "ftell",
    "untar",
    "deployprefdir",
    "matlabroot",
    "instrcb",
    "textscan",
    "fwrite",
    "textread",
    "fgets",
    "parseSoapResponse",
    "xlsfinfo",
    "timercb",
    "fclose",
]

import itertools

from mat2py.common.backends import numpy as np
from mat2py.common.backends import py_zip
from mat2py.common.logger import logger

from ._internal.array import M, mp_convert_scalar
from ._internal.helper import mp_inference_nargout_decorators
from ._internal.object_handles import FileIdentifier, openedFiles


def home(*args):
    raise NotImplementedError("home")


def partialpath(*args):
    raise NotImplementedError("partialpath")


def filemarker(*args):
    raise NotImplementedError("filemarker")


def xlsread(*args):
    raise NotImplementedError("xlsread")


def fscanf(*args):
    raise NotImplementedError("fscanf")


def tempdir(*args):
    raise NotImplementedError("tempdir")


def clc(*args):
    pass


def csvread(*args):
    raise NotImplementedError("csvread")


def xslt(*args):
    raise NotImplementedError("xslt")


def dataread(*args):
    raise NotImplementedError("dataread")


def unzip(*args):
    raise NotImplementedError("unzip")


def fileparts(*args):
    raise NotImplementedError("fileparts")


def mltimerpackage(*args):
    raise NotImplementedError("mltimerpackage")


def createClassFromWsdl(*args):
    raise NotImplementedError("createClassFromWsdl")


@mp_inference_nargout_decorators()
def fopen(filename, *args, nargout=None):
    if filename == "all":
        return (M[openedFiles.keys()],)

    if nargout > 1:
        raise NotImplementedError("fopen")

    filename = mp_convert_scalar(filename)
    if isinstance(filename, FileIdentifier):
        return (openedFiles.get_name(filename),)

    permission = "r"
    if args:
        permission = args[0]
        if len(args) > 1:
            logger.warning('NotImplementedError("fopen")')

    try:
        fp = open(filename, permission, buffering=1)
        return (openedFiles.insert(fp, start_id=3),)
    except Exception as err:
        logger.warning(err)
        return (FileIdentifier(-1),)


def zip(*args):
    raise NotImplementedError("zip")


def fseek(*args):
    raise NotImplementedError("fseek")


def prefdir(*args):
    raise NotImplementedError("prefdir")


def sendmail(*args):
    raise NotImplementedError("sendmail")


def dlmwrite(*args):
    raise NotImplementedError("dlmwrite")


def matfile(*args):
    raise NotImplementedError("matfile")


def urlwrite(*args):
    raise NotImplementedError("urlwrite")


def callSoapService(*args):
    raise NotImplementedError("callSoapService")


def timerfindall(*args):
    raise NotImplementedError("timerfindall")


def createSoapMessage(*args):
    raise NotImplementedError("createSoapMessage")


def xmlwrite(*args):
    raise NotImplementedError("xmlwrite")


def dlmread(*args):
    raise NotImplementedError("dlmread")


def fprintf(fileID, formatSpec, *args):
    if not isinstance(fileID, FileIdentifier):
        fileID, formatSpec, args = 1, fileID, (formatSpec, *args)

    if isinstance(formatSpec, np.ndarray):
        formatSpec = "".join(formatSpec.reshape(-1).tolist())

    content = formatSpec
    n = formatSpec.count("%") - 2 * formatSpec.count("%%")
    if args and n > 0:
        # Matlab actually support incomplete format but mat2py will drop the last in-complete one
        # assert sum(np.size(a) if isinstance(a, np.ndarray) else 1 for a in args)%n == 0
        args = itertools.chain.from_iterable(
            a.reshape(-1, order="F").tolist() if isinstance(a, np.ndarray) else (a,)
            for a in args
        )
        content = "".join(formatSpec % arg for arg in py_zip(*[args] * n))

    openedFiles.get_fp(fileID).write(content)
    return len(content)


def importdata(*args):
    raise NotImplementedError("importdata")


def readtable(*args):
    raise NotImplementedError("readtable")


def fileread(*args):
    raise NotImplementedError("fileread")


def fgetl(*args):
    raise NotImplementedError("fgetl")


def pathsep(*args):
    raise NotImplementedError("pathsep")


def xlswrite(*args):
    raise NotImplementedError("xlswrite")


def gzip(*args):
    raise NotImplementedError("gzip")


def feof(*args):
    raise NotImplementedError("feof")


def ferror(*args):
    raise NotImplementedError("ferror")


def tempname(*args):
    raise NotImplementedError("tempname")


def daqread(*args):
    raise NotImplementedError("daqread")


def xmlread(*args):
    raise NotImplementedError("xmlread")


def fullfile(*args):
    raise NotImplementedError("fullfile")


def fread(*args):
    raise NotImplementedError("fread")


def frewind(*args):
    raise NotImplementedError("frewind")


def gunzip(*args):
    raise NotImplementedError("gunzip")


def urlread(*args):
    raise NotImplementedError("urlread")


def instrfind(*args):
    raise NotImplementedError("instrfind")


def matfinfo(*args):
    raise NotImplementedError("matfinfo")


def tar(*args):
    raise NotImplementedError("tar")


def fileExchangeDesktopTool(*args):
    raise NotImplementedError("fileExchangeDesktopTool")


def instrfindall(*args):
    raise NotImplementedError("instrfindall")


def csvwrite(*args):
    raise NotImplementedError("csvwrite")


def filesep(*args):
    raise NotImplementedError("filesep")


def writetable(*args):
    raise NotImplementedError("writetable")


def timerfind(*args):
    raise NotImplementedError("timerfind")


def ftell(*args):
    raise NotImplementedError("ftell")


def untar(*args):
    raise NotImplementedError("untar")


def deployprefdir(*args):
    raise NotImplementedError("deployprefdir")


def matlabroot(*args):
    raise NotImplementedError("matlabroot")


def instrcb(*args):
    raise NotImplementedError("instrcb")


def textscan(*args):
    raise NotImplementedError("textscan")


def fwrite(*args):
    raise NotImplementedError("fwrite")


def textread(*args):
    raise NotImplementedError("textread")


def fgets(*args):
    raise NotImplementedError("fgets")


def parseSoapResponse(*args):
    raise NotImplementedError("parseSoapResponse")


def xlsfinfo(*args):
    raise NotImplementedError("xlsfinfo")


def timercb(*args):
    raise NotImplementedError("timercb")


def fclose(fileID: FileIdentifier):
    fileIDs = openedFiles.keys() if fileID == "all" else (fileID,)
    try:
        for f in fileIDs:
            openedFiles.pop(f).close()
        return 0
    except Exception as err:
        logger.warning(err)
        return -1
