__all__ = ["logger"]

import logging
import logging.config
from io import StringIO

from mat2py.config import Config

default_logging_template = """
;; loggers list
[loggers]
keys = root,mp2console,mp2file

[logger_root]
level = {root_logger_level}
handlers = basic
propagate = 0

[logger_mp2console]
level = {logging_level}
handlers = console
qualname = mat2py
propagate = 0

[logger_mp2file]
level = {logging_level}
handlers = console,file
qualname = mat2py.file
propagate = 0

;; handlers list
[handlers]
keys = basic,null,console,file

[handler_basic]
class = StreamHandler
formatter = basic
args = (sys.stderr,)

[handler_null]
;; do nothing
class = NullHandler

[handler_console]
class = StreamHandler
formatter = simple
args = (sys.stderr,)

[handler_file]
class = FileHandler
formatter = simple
args = ('{logging_file}', 'a', None, True)

;; formatters list
[formatters]
keys = basic,simple

[formatter_basic]
format = %(levelname)s:%(name)s:%(message)s

[formatter_simple]
format = %(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt = %Y-%m-%d,%H:%M:%S
"""

mat2py_config = Config()
logging_config = mat2py_config.logging_config
if isinstance(logging_config, dict):
    logging_config = default_logging_template.format_map(logging_config)

logging.config.fileConfig(StringIO(logging_config), disable_existing_loggers=False)

logger = logging.getLogger(mat2py_config.default_logger)
