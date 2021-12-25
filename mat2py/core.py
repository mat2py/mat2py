# type: ignore
import typing
from typing import Callable, Tuple, Union

import operator

import numpy as np

__all__ = ["pi", "eps", "end", "colon"]

pi = np.pi
eps = np.finfo(float).eps


class End:
    def __init__(self, expr=None):
        self.expr = expr if expr is not None else [None]

    def __call__(self, length: int) -> int:
        if length is None:
            raise ValueError("length can not be None when evaluating End")
        tokens = [length if i is None else i for i in self.expr]

        stack = []
        for token in tokens:
            if type(token).__name__ != "builtin_function_or_method":
                stack.append(token)
            else:
                if token is operator.neg:
                    stack.append(-stack.pop())
                else:
                    rhs = stack.pop()
                    stack[-1] = token(stack[-1], rhs)

        assert len(stack) == 1
        return round(stack[0])

    def __binary_operator(self, other: Union[int, "End"], op: typing.Callable) -> "End":
        rhs = other.expr if isinstance(other, self.__class__) else [other]
        return self.__class__([*self.expr, *rhs, op])

    def __radd__(self, other: int) -> "End":
        return self.__class__([other, *self.expr, operator.add])

    def __rsub__(self, other: (int, "End")) -> "End":
        return self.__class__([other, *self.expr, operator.sub])

    def __add__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.add)

    def __sub__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.sub)

    def __mod__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.mod)

    def __mul__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.mul)

    def __pow__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.pow)

    def __floordiv__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.floordiv)

    def __truediv__(self, other: (int, "End")) -> "End":
        return self.__binary_operator(other, operator.truediv)

    def __pos__(self) -> "End":
        return self

    def __neg__(self) -> "End":
        return self.__class__([*self.expr, operator.neg])


end = End()


class Colon:
    def __init__(
        self, start: (float, End), stop: (float, End), step: (float, End) = None
    ):
        self.range = (
            start,
            1 if step is None else stop,
            stop if step is None else step,
        )

    def __iter__(self):
        if not isinstance(self.range, np.ndarray):
            self.to_array()
        return iter(self.range)

    def to_slice(self, length=None) -> slice:
        assert isinstance(self.range, tuple)

        start, step, stop = map(
            round,
            tuple(
                expr(length) if isinstance(expr, End) else expr for expr in self.range
            ),
        )

        if stop > length:
            raise ValueError(f"out of the dimension")
        if start < 1:
            raise ValueError(f"index must be positive integer")
        start -= 1
        return slice(start, max(stop, start), step)

    def to_array(self) -> "Array":
        if not isinstance(self.range, np.ndarray):
            if any(isinstance(expr, End) for expr in self.range):
                raise ValueError("range can not contain end expression")
            start, step, stop = self.range
            self.range = np.arange(start, stop + step / 10.0, step).view(Array)

        return self.range


def colon(*args):
    return Colon(*args)


class Array(np.ndarray):
    """https://numpy.org/doc/stable/user/basics.subclassing.html"""

    def __call__(self, item):
        return self.__getitem__(item)

    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, item):
        return super().__getitem__(item - 1)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)


def array(*args, **kwargs):
    return np.array(*args, **kwargs).view(Array)


if __name__ == "__main__":
    x = array([1, 2, 3])

    print(x(1), x.shape)
