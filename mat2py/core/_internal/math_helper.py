# type: ignore
import functools

from mat2py.common.backends import numpy as np

from .array import M, mp_convert_round, mp_convert_scalar
from .helper import (
    mp_inference_nargout_decorators,
    mp_last_arg_as_kwarg,
    mp_nargout_from_stack,
)


@functools.lru_cache(maxsize=10)
def mp_sum_like_decorators(default_if_empty=None):
    def decorator(func):
        @functools.wraps(func)
        @mp_last_arg_as_kwarg("all_elements", ("all",))
        def wrapper(x, *args, all_elements=False):
            if all_elements:
                assert not args
                return M[func(x)]
            if np.size(x) == 0 and default_if_empty is not None:
                return default_if_empty
            dim = (
                mp_convert_scalar(args[0]) - 1
                if args
                else np.argmax(M[np.shape(x)] > 1)
            )
            res = func(x, mp_convert_round(dim), keepdims=True)
            r = np.argmax(np.array(np.shape(res))[::-1] > 1)
            if r > 0 and np.ndim(x) - r > 1:
                res = res.reshape(res.shape[:-r])
            return M[res]

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_max_like_decorators():
    def decorator(func, argfunc, pfunc, nanfunc):
        @functools.wraps(func)
        @mp_inference_nargout_decorators()
        @mp_last_arg_as_kwarg("nanflag", ("omitnan", "includenan"))
        def wrapper(*args, nanflag="omitnan", nargout=None):
            if nargout == 2:
                # argfunc(*args)
                raise NotImplementedError

            assert nargout == 1
            if (len(args) == 1) or (
                len(args) > 1
                and isinstance(args[1], np.ndarray)
                and np.size(args[1]) == 0
            ):
                return (
                    mp_sum_like_decorators()(nanfunc if nanflag == "omitnan" else func)(
                        args[0], *args[2:]
                    ),
                )
            else:
                return (M[pfunc(*args)],)

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_zeros_like_decorators(expand_shape=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            args = tuple(mp_convert_scalar(i) for i in args)
            dtype = np.float_
            shape = args
            if len(args) >= 2 and args[-2] == "like":
                dtype = M[args[-1]].dtype
                shape = args[:-2]
            elif isinstance(args[-1], str):
                classname = args[-1]
                dtype = {
                    "double": np.float64,
                    "single": np.float32,
                }.get(classname, getattr(np, classname))
                shape = args[:-1]

            if len(shape) == 0:
                shape = (1, 1)
            elif len(shape) == 1 and isinstance(shape[0], np.ndarray):
                shape = shape[0].reshape(-1).tolist()
            elif len(shape) == 1:
                shape = (shape[0], shape[0])
            shape = tuple(mp_convert_round(s) for s in shape)
            if expand_shape:
                return M[func(*shape, dtype=dtype)]
            else:
                return M[func(shape, dtype=dtype)]

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_rand_like_decorators():
    def decorator(func):
        @functools.wraps(func)
        @mp_zeros_like_decorators(expand_shape=True)
        def wrapper(*args, dtype=None):
            a = func(*args)
            if not np.issubdtype(a.dtype, dtype):
                a = a.astype(dtype)
            return a

        return wrapper

    return decorator
