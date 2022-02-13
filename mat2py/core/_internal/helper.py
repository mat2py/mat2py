# type: ignore
import functools

from .array import M


@functools.lru_cache(maxsize=10)
def matlab_function_decorators(nargout: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            obj = func(*args, **kwargs)
            if nargout == 1:
                return M[obj]
            else:
                raise NotImplementedError

        return wrapper

    return decorator


def special_variables(value: float, name: str = ""):
    return value
