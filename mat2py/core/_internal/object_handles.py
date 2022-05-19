# type: ignore

import sys

from mat2py.common.utils import Singleton

FileIdentifier = int


class OpenedObjects(dict):
    def insert(self, handle, start_id=1):
        id = next(i for i in range(start_id, len(self) + start_id + 1) if i not in self)
        self[id] = handle
        return id


class OpenedFiles(OpenedObjects, metaclass=Singleton):
    def get_fp(self, id: FileIdentifier):
        return (sys.stdin, sys.stdout, sys.stderr)[id] if id < 3 else self[id]

    def get_name(self, id: FileIdentifier):
        return ("stdin", "stdout", "stderr")[id] if id < 3 else self[id].name


openedFiles = OpenedFiles()
