__all__ = ["Config"]
from typing import Union

import logging
from logging import WARNING, getLevelName

from mat2py.common.utils import Singleton


class Config(metaclass=Singleton):
    def __init__(self):
        self.ignore_nargout_inference_exception = False
        self.logging_options = {
            "root_logger_level": logging.getLevelName(
                logging.getLogger().getEffectiveLevel()
            ),
            "logging_level": getLevelName(WARNING),
            "logging_file": "mat2py.log",
        }
        self.default_logger = "mat2py"

    @property
    def set_default_nargout(self):
        return self.ignore_nargout_inference_exception

    @set_default_nargout.setter
    def set_default_nargout(self, toggle: bool = True) -> None:
        self.ignore_nargout_inference_exception = toggle

    @property
    def logging_level(self):
        return self.logging_options["logging_level"]

    @logging_level.setter
    def logging_level(self, level: Union[int, str]) -> None:
        self.logging_options["logging_level"] = (
            level if isinstance(level, str) else getLevelName(level)
        )

    @property
    def logging_file(self):
        return self.logging_options["logging_file"]

    @logging_file.setter
    def logging_file(self, filename: str) -> None:
        self.logging_options["logging_file"] = filename
        self.default_logger = "mat2py.file"

    @property
    def logging_config(self):
        return self.logging_options
