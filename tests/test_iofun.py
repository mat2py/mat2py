# type: ignore
from pathlib import Path

import pytest

from .helper import *


def test_fprintf():
    filename = "test_fprintf.log"
    fileID = fopen(filename, "w")
    assert fopen(fileID) == filename
    fprintf(fileID, "filename: %s\n", filename)

    A1 = M[[9.9, 9900]]
    A2 = M[
        [8.8, 7.7],
        [8800, 7700],
    ]
    formatSpec = "X is %4.2f meters or %8.3f mm\n"
    fprintf(fileID, formatSpec, A1, A2)

    fclose(fileID)

    assert Path(filename).read_text() == (
        f"filename: {filename}\n"
        "X is 9.90 meters or 9900.000 mm\n"
        "X is 8.80 meters or 8800.000 mm\n"
        "X is 7.70 meters or 7700.000 mm\n"
    )
    Path(filename).unlink()
