# type: ignore
from io import StringIO
from pathlib import Path

import pytest

from mat2py.core._internal.object_handles import openedFiles

from .helper import *


def test_fprintf():
    with StringIO() as fp:
        filename = "test_fprintf.log"
        # 1st way: Use fopen/fclose from Matlab
        # fileID = fopen(filename, "w")

        # 2nd way: Insert the file object directly into Mat2Py backend
        fp.name = filename
        fileID = openedFiles.insert(
            fp, start_id=3
        )  # Notice: must start from 3 as 0,1,2 reserved for std
        assert fopen(fileID) == filename
        fprintf(fileID, "filename: %s\n", filename)

        A1 = M[[9.9, 9900]]
        A2 = M[
            [8.8, 7.7],
            [8800, 7700],
        ]
        formatSpec = "X is %4.2f meters or %8.3f mm\n"
        fprintf(fileID, formatSpec, A1, A2)

        # fclose(fileID)
        openedFiles.pop(fileID)  # Notice: do not forget to remove it from tracking

        content = (
            f"filename: {filename}\n"
            "X is 9.90 meters or 9900.000 mm\n"
            "X is 8.80 meters or 8800.000 mm\n"
            "X is 7.70 meters or 7700.000 mm\n"
        )

        assert fp.getvalue() == content
        # assert Path(filename).read_text() == content
        # Path(filename).unlink()
