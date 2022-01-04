# type: ignore
import typing
from typing import Callable, Tuple, Union

import operator
from functools import reduce

import numpy as np

__all__ = ["pi", "eps", "end", "I"]

pi = np.pi
eps = np.finfo(float).eps * 10.0  # we use a little larger eps than Numpy


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
    """colon equivelent in Matlab"""

    """ It should be (start, stop) format or (start, step, stop) format. """
    """ Colon used for array indexing (1-based Matlab format) will be converted to slice (0-based Python format); """
    """ Colon used for generating sequence will be converted to np.arange while keeping the right end point."""

    def __init__(
        self, start: (float, End), stop: (float, End), step: (float, End) = None
    ):
        assert start is not None and stop is not None
        self.range = (  # in (start, stop, step) order
            start,
            stop,
            1 if step is None else step,
        )

        # TODO: general function for converting to MatArray

    def __sub__(self, i: int):
        if isinstance(self.range, tuple):
            return self.__class__(self.range[0] - i, self.range[1] - i, self.range[1])
        else:
            return self.range - i

    def __iter__(self):
        if isinstance(self.range, tuple):
            self.to_array()
        return iter(self.range)

    def to_index(self, length=None) -> slice:
        if isinstance(self.range, tuple):
            start, stop, step = map(
                round,
                tuple(
                    expr(length) if isinstance(expr, End) else expr
                    for expr in self.range
                ),
            )
            # TODO: validation on [1, length]
            if stop > length:
                raise ValueError(f"out of the dimension")
            if start < 1:
                raise ValueError(f"index must be positive integer")

            return slice(
                start - 1,
                max(stop, start - 1) if step > 0 else min(stop, start - 1),
                step,
            )
        else:
            return np.round(self.range).astype(int) - 1

    def to_array(self) -> "MatArray":
        if isinstance(self.range, tuple):
            if any(isinstance(expr, End) for expr in self.range):
                raise ValueError("range can not contain end expression")

            start, stop, step = self.range
            stop += 1 if np.issubdtype(np.array(self.range).dtype, np.integer) else eps

            self.range = np.arange(start, stop, step).view(MatArray)

        return self.range


def colon(*args):
    if len(args) == 2:
        return Colon(*args)
    elif len(args) == 3:
        return Colon(args[0], args[2], args[1])
    if len(args) == 1 and isinstance(args[0], slice):
        item = args[0]
        if item.step is not None:
            return Colon(item.start, item.step, item.stop)
        else:
            return Colon(
                item.start if item.start is not None else 1,
                item.stop if item.stop is not None else end,
                1,
            )
    else:
        raise ValueError("colon can only accept i:k or i:j:k format")


class MatIndex:
    def __init__(self, index):
        self.item = index.item if isinstance(index, MatIndex) else index

    @staticmethod
    def __getitem__(item):
        return MatIndex(item)

    @staticmethod
    def __convert(item: (Colon, slice, End, "MatIndex", int, np.ndarray), length: int):
        if isinstance(item, Colon):
            return item.to_index(length)
        elif isinstance(item, slice):
            return colon(item).to_index(length)
        elif isinstance(item, End):
            return item(length) - 1
        elif isinstance(item, MatIndex):
            return item((length,))
        else:
            return item - 1

    def __call__(self, shape: Tuple[int]):
        item = self.item if isinstance(self.item, tuple) else (self.item,)

        if len(item) == len(shape):
            return tuple(self.__convert(i, l) for i, l in zip(item, shape))
        if len(item) == 1:  # line index
            return ind2sub(shape, self.__convert(item[0], reduce(operator.mul, shape)))
        elif len(self.item) < len(shape):
            raise NotImplementedError

        raise ValueError("index exceed the Array dimention")


I = MatIndex(None)


def ind2sub(shape: tuple, index: (typing.Iterable[int], int, slice)):
    if len(shape) == 1:
        return index
    elif len(shape) == 2:
        d1, d2 = shape
        index = (
            np.array(index).reshape(-1)
            if not isinstance(index, slice)
            else np.arange(index.start, index.stop, index.step)
        )
        return (index % d1, index // d1)
    else:
        # TODO: take care of fortran order
        raise NotImplementedError


class MatArray(np.ndarray):
    """https://numpy.org/doc/stable/user/basics.subclassing.html"""

    def __call__(self, item, *rest_item):
        # TODO: we can not differicate `a(1)` and `a(1,)` while `a[1]` and `a[1,]` have difference
        item = [item, *rest_item] if rest_item else item
        return super().__getitem__(MatIndex(item)(self.shape))

    def __iter__(self):
        raise NotImplementedError

    def __getitem__(self, item):
        if isinstance(item, End):
            item = MatIndex(item)
        if isinstance(item, MatIndex):
            item = item(self.shape)
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        if isinstance(key, End):
            key = MatIndex(key)
        if isinstance(key, MatIndex):
            key = key(self.shape)

        return super().__setitem__(key, value)


def array(*args, **kwargs):
    return np.array(*args, **kwargs).view(MatArray)


clc = None
clear = None
disp = print
error = print
exp = np.exp
linspace = np.linspace
ndgrid = np.meshgrid

numel = np.size
randn = np.random.randn
rng = np.random.default_rng
sinc = np.sinc
size = np.shape
