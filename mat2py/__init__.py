"""mat2py mean to be drop-in replacement of Matlab by wrapping Numpy/Scipy/... packages."""

from .config import Config
from .version import get_version

version: str = get_version()
__version__: str = version

config: Config = Config()
