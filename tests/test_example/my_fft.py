# type: ignore

import mat2py as mp
from mat2py.core import *


def my_fft(x):
    N = mp.numel(x)
    xp = x[mp.colon(1, 2, end)]
    xpp = x[mp.colon(2, 2, end)]
    if N >= 8:
        Xp = my_fft(xp)
        Xpp = my_fft(xpp)
        Wn = mp.exp(
            mp.mrdivide(
                mp.dot(
                    mp.dot(mp.dot(-1j, 2), pi), (mp.colon(0, (mp.mrdivide(N, 2)) - 1)).T
                ),
                N,
            )
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
            mp.error("N not correct.")
    return X


def main():
    mp.rng("default")
    t = mp.colon(1, 10)
    x = (mp.randn(mp.size(t))).T
    ts = mp.linspace(-5, 15, 2 ^ 9)
    Ts, T = mp.ndgrid(ts, t)
    y = mp.dot(mp.sinc(Ts - T), x)
    f = my_fft(y)
    mp.disp(mp.array([y, f]))


if __name__ == "__main__":
    main()
