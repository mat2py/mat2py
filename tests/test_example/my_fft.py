# type: ignore

import mat2py.core as mp
from mat2py.core import (
    I,
    M,
    clc,
    clear,
    colon,
    disp,
    end,
    error,
    exp,
    linspace,
    mrdivide,
    mtimes,
    ndgrid,
    numel,
    pi,
    randn,
    rng,
    sinc,
    size,
)


def my_fft(x):
    N = numel(x)
    xp = x[I[1:2:end]]
    xpp = x[I[2:2:end]]
    if N >= 8:
        Xp = my_fft(xp)
        Xpp = my_fft(xpp)
        Wn = exp(
            mrdivide(mtimes(mtimes((-1j) * 2, pi), (colon(0, ((N / 2) - 1))).T), N)
        )
        tmp = Wn * Xpp
        X = M[
            Xp + tmp,
            Xp - tmp,
        ]
    else:
        if N == 2:
            X = mtimes(
                M[
                    [1, 1],
                    [1, -1],
                ],
                x,
            )
        elif N == 4:
            X = mtimes(
                mtimes(
                    M[
                        [1, 0, 1, 0],
                        [0, 1, 0, -1j],
                        [1, 0, -1, 0],
                        [0, 1, 0, 1j],
                    ],
                    M[
                        [1, 0, 1, 0],
                        [1, 0, -1, 0],
                        [0, 1, 0, 1],
                        [0, 1, 0, -1],
                    ],
                ),
                x,
            )
        else:
            error("N not correct.")
    return X


def main():
    clear
    clc
    rng("default")
    t = colon(1, 10)
    x = randn(size(t)).T
    ts = linspace(-5, 15, 2 ^ 9)
    Ts, T = ndgrid(ts, t)
    y = mtimes(sinc(Ts - T), x)
    f = my_fft(y)
    disp(M[[y, f]])


if __name__ == "__main__":
    main()
