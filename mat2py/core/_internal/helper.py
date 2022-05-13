# type: ignore
import ast
import functools
import re
from copy import deepcopy
from inspect import stack
from pathlib import Path

import executing

from mat2py.common.backends import numpy as np
from mat2py.common.utils import Singleton

from .array import M, mp_detect_vector


@functools.lru_cache(maxsize=10)
def mp_last_arg_as_kwarg(key: str, value_map: (tuple, dict)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args and isinstance(args[-1], str) and args[-1] in value_map:
                if isinstance(value_map, dict):
                    value = value_map[args[-1]]
                elif isinstance(value_map, tuple):
                    value = True if len(value_map) == 1 else args[-1]
                kwargs = {**kwargs, key: value}
                args = args[:-1]
            return func(*args, **kwargs)

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_match_vector_direction(match_arg_position=0, target_arg_position: tuple = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if len(args) <= match_arg_position:
                return res
            vec_type = mp_detect_vector(args[match_arg_position])
            if vec_type == 0:
                return res
            new_res = (
                list(res)
                if isinstance(res, tuple)
                else [
                    res,
                ]
            )

            for i in (
                range(len(new_res))
                if target_arg_position is None
                else target_arg_position
            ):
                res_vec_type = mp_detect_vector(new_res[i])
                if res_vec_type != 0 and res_vec_type != vec_type:
                    new_res[i] = new_res[i].reshape(
                        (1, -1) if vec_type == 1 else (-1, 1)
                    )

            return tuple(new_res) if isinstance(res, tuple) else new_res[0]

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_argout_wrapper_decorators(nargout: int = 1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            obj = func(*args, **kwargs)
            if nargout == 1:
                return M[obj]
            else:
                assert isinstance(obj, tuple)
                return tuple(M[o] for o in obj)

        return wrapper

    return decorator


def mp_special_variables(value: float, name: str = ""):
    return value


@functools.lru_cache(maxsize=10)
def mp_pass_values_decorators(args_position: tuple = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args = list(args)
            # TODO: can we detect temporary right value and avoid deepcopy for throughput? e.g. sys.getrefcount()
            if args_position is None:
                return func(*deepcopy(args), **kwargs)

            for p in args_position:
                if p < len(args):
                    args[p] = deepcopy(args[p])
            return func(*args, **kwargs)

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_inference_nargout_decorators(caller_level: int = 2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, nargout=None, **kwargs):
            if nargout is None:
                nargout = mp_nargout_from_stack(caller_level, func)
            res = func(*args, **kwargs, nargout=nargout)
            if not isinstance(res, tuple):
                # TODO: we should be smarter
                raise SyntaxWarning(
                    "mp_inference_nargout_decorators can only be used once"
                )
            return res[0] if nargout == 1 else res[:nargout]

        return wrapper

    return decorator


@functools.lru_cache(maxsize=10)
def mp_inference_nargin_decorators():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            return func(*args, nargin=len(args))

        return wrapper

    return decorator


class CodeContext(metaclass=Singleton):
    def __init__(self):
        self.code = None
        self.__ast__ = None
        # for console_mode, co_filename and f_lineno will be ignored
        self.console_mode = False

    def init(self, console_mode=True):
        self.code = None
        self.__ast__ = None
        self.console_mode = console_mode

    @property
    def ast(self):
        if self.__ast__ is None:
            self.__ast__ = ast.parse(self.code).body[0]

        return self.__ast__

    def __call__(self, code: str):
        code = code.strip()
        if code is not "" and code != self.code:
            self.code = code
            self.__ast__ = None

        return self


def mp_nargout_from_ast(ast_tree, func_name: str):
    if (
        isinstance(ast_tree, ast.Assign)
        and isinstance(ast_tree.value, ast.Call)
        and ast_tree.value.func.id == func_name
        and isinstance(
            ast_tree.targets[0], ast.Tuple
        )  # `a, = func()` not allowed in matlab
    ):
        return len(ast_tree.targets[0].elts)
    else:
        return 1


def mp_nargout_from_stack(caller_level: int = 2, func=None):
    current, *_, caller = stack()[1 : (caller_level + 1)]
    function = func.__name__ if func is not None else current.function

    try:
        frame_meta = executing.Source.executing(caller.frame)
        if frame_meta.node is not None:
            call_node = frame_meta.node
            assert isinstance(call_node, ast.Call) and call_node.func.id == function
            return mp_nargout_from_ast(call_node.parent, function)
        else:
            # TODO: what if multiple statement in one line? how to handle multiple call with same function?
            (ast_tree,) = frame_meta.statements
            return mp_nargout_from_ast(ast_tree, function)
    except Exception as err:
        code_context = "\n".join(caller.code_context or []).strip()
        context = CodeContext()
        tree_ast = context(code_context).ast

        raise SyntaxWarning(
            "failed to inference nargout from call stack, pass the information explicitly"
        )
