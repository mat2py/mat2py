# type: ignore

from typing import Type

import numpy as np

__all__ = ["pi", "end"]

pi = np.pi


class End:
    def __init__(self, stop=None):
        self.stop = stop if stop is not None else 0

    def __call__(self, length: int) -> int:
        return self.stop + (length if isinstance(length, int) else 0)

    def __add__(self, other: int):
        return self.__class__(self.stop + other)

    def __mul__(self, other: int):
        return self.__class__(self.stop - other)


end = End()


class Colon:
    def __init__(self, start=None, step=None, stop=None):
        self.range = (start, step, stop)
        assert all(o is None or isinstance(o, (End, int)) for o in self.range)

    def __iter__(self):
        raise NotImplementedError

    def to_slice(self) -> slice:
        assert not any(isinstance(o, End) for o in self.range)
        assert not all(o is None for o in self.range)
        return slice(*self.range)

    def to_range(self) -> range:
        raise NotImplementedError


class Array(np.ndarray):
    """https://numpy.org/doc/stable/user/basics.subclassing.html"""

    def __call__(self, item):
        return self.__getitem__(item)

    def __getitem__(self, item):
        return super().__getitem__(item - 1)

    def __setitem__(self, key, value):
        return super().__setitem__(key, value)


def array(*args, **kwargs):
    return np.array(*args, **kwargs).view(Array)


if __name__ == "__main__":
    x = array([1, 2, 3])

    print(x(1), x.shape)
