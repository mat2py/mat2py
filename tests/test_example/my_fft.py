# type: ignore

import mat2py.core as mp
from mat2py.core import (
    I,
    clc,
    clear,
    disp,
    end,
    error,
    exp,
    linspace,
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
            mp.mrdivide(mp.dot(mp.dot((-1j) * 2, pi), (colon(0, ((N / 2) - 1))).T), N)
        )
        tmp = Wn * Xpp
        X = mp.stack((Xp + tmp, Xp - tmp))
    else:
        if N == 2:
            X = mp.dot(mp.stack(([1, 1], [1, -1])), x)
        elif N == 4:
            X = mp.dot(
                mp.dot(
                    mp.stack(
                        ([1, 0, 1, 0], [0, 1, 0, -1j], [1, 0, -1, 0], [0, 1, 0, 1j])
                    ),
                    mp.stack(
                        ([1, 0, 1, 0], [1, 0, -1, 0], [0, 1, 0, 1], [0, 1, 0, -1])
                    ),
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
    t = I[1:10]
    x = randn(size(t)).T
    ts = linspace(-5, 15, 2 ^ 9)
    Ts, T = ndgrid(ts, t)
    y = mp.dot(sinc(Ts - T), x)
    f = my_fft(y)
    disp(mp.array([y, f]))


if __name__ == "__main__":
    main()
