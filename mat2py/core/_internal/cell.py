# type: ignore

from types import SimpleNamespace

from mat2py.common.backends import numpy as np

from .array import M, MatArray, _convert_round, _convert_scalar, _convert_to_2d


class CellArray(MatArray):
    def __call__(self, item, *rest_item):
        if rest_item:
            item = (item, *rest_item)
        return self.__getitem__(item)

    def __getitem__(self, item):
        c = self.view(MatArray).__getitem__(item)
        if isinstance(c, SimpleNamespace):
            return c.obj

        assert isinstance(c, MatArray) and c.dtype == object
        if np.size(c) == 1:
            return c.reshape(-1)[0].obj
        else:
            return c.view(CellArray)

    def __setitem__(self, key, value):
        c = self.view(MatArray)[key]
        if isinstance(c, SimpleNamespace):
            c.obj = value
        else:
            assert isinstance(c, MatArray) and c.dtype == object
            if np.size(c) == 1:
                # we only support c{1} case, c(1) need redesign of CellArray
                c = c.reshape(-1)[0]
                assert isinstance(c, SimpleNamespace)
                c.obj = value
            elif np.size(c) > 1:
                # c(1:end) case
                assert isinstance(value, CellArray)
                value = _convert_to_2d(value.view(MatArray), c.shape)
                assert value.shape == c.shape
                super().__setitem__(key, value)
        return self

    def __array_ufunc__(self, *args, **kwargs):
        raise NotImplementedError("cell do not support calculation")


class C(type):
    @staticmethod
    def __class_getitem__(args) -> CellArray:
        if not isinstance(args, tuple):
            args = (args,)
        data = [
            [
                SimpleNamespace(obj=c)
                for c in (
                    r
                    if isinstance(r, list)
                    else [
                        r,
                    ]
                )
            ]
            for r in args
        ]
        return np.array(data, dtype=object).view(CellArray)


def cell(n, *args):
    if args:
        shape = (n, *args)
    else:
        n = _convert_scalar(n)
        if np.ndim(n) == 0:
            shape = (n, n)
        elif np.ndim(n) <= 2 and np.size(n) == np.shape(n)[-1]:
            shape = n.reshape(-1, order="F").tolist()
        else:
            raise ValueError("invalid shape")
    shape = tuple(_convert_round(_convert_scalar(i)) for i in shape)
    obj = np.array(
        [SimpleNamespace(obj=M[[]]) for _ in range(np.prod(shape))], dtype=object
    ).reshape(shape)
    return obj.view(CellArray)
