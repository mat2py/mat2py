# type: ignore
import ast
import functools
import re
from inspect import stack
from lib2to3.fixer_base import BaseFix
from lib2to3.refactor import RefactoringTool
from pathlib import Path

from .array import M


@functools.lru_cache(maxsize=10)
def argout_wrapper_decorators(nargout: int = 1):
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


def special_variables(value: float, name: str = ""):
    return value


# see https://stackoverflow.com/questions/58720279/python-inspect-stacks-code-context-only-returns-one-line-of-context
class StatementScraper(BaseFix):
    PATTERN = "simple_stmt"

    def __init__(self, lineno):
        super().__init__(None, None)
        self.lineno = lineno
        self.statement = ""

    def transform(self, node, result):
        if not self.statement and self.lineno - node.get_lineno() < str(node).count(
            "\n"
        ):
            prev_sibling = str(node.prev_sibling)
            if prev_sibling.isspace():
                self.statement += prev_sibling.lstrip("\n")
            self.statement += str(node)
        return node


class GetStatement(RefactoringTool):
    def __init__(self, source, lineno):
        self.source = source
        self.scraper = StatementScraper(lineno)
        super().__init__(None)

    def get_fixers(self):
        return [self.scraper], []

    def __str__(self):
        self.refactor_string(self.source, "")
        return self.scraper.statement


@functools.lru_cache(maxsize=50)
def nargout_from_ast(s: str, func_name: str, co_filename=None, f_lineno=None):
    try:
        if s is None:
            raise SyntaxError
        tree = ast.parse(s.strip()).body[0]
    except SyntaxError:
        s = str(GetStatement(Path(co_filename).read_text(), f_lineno))
        tree = ast.parse(s.strip()).body[0]

    if (
        isinstance(tree, ast.Assign)
        and isinstance(tree.value, ast.Call)
        and tree.value.func.id == func_name
        and isinstance(
            tree.targets[0], ast.Tuple
        )  # `a, = func()` not allowed in matlab
    ):
        return len(tree.targets[0].elts)
    else:
        return 1


def nargout_from_stack():
    try:
        current, caller = stack()[1:3]
        frame = caller.frame
        code_context = "\n".join(caller.code_context).strip()
        return nargout_from_ast(
            code_context
            if re.match(r'[^\'"]+\s*=\s*' + current.function, code_context)
            else None,
            current.function,
            frame.f_code.co_filename,
            frame.f_lineno,
        )
    except (AttributeError, IndexError):
        return 1
