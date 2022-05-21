__all__ = ["Singleton", "action_on_warnings"]

from typing import Dict

import warnings
from functools import wraps


class Singleton(type):
    _instances: Dict[type, object] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def action_on_warnings(action="error", category=Warning):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with warnings.catch_warnings():
                warnings.simplefilter(action, category)
                return func(*args, **kwargs)

        return wrapper

    return decorator
