# type: ignore

from .helper import *


def test_inpolygon():
    xv = rand(6, 1)
    yv = rand(6, 1)
    xv = M[
        xv,
        xv(1),
    ]
    yv = M[
        yv,
        yv(1),
    ]
    x = rand(1000, 1)
    y = rand(1000, 1)
    _in = inpolygon(x, y, xv, yv)
    plot(xv, yv, x(_in), y(_in), ".r", x(_not(_in)), y(_not(_in)), ".b")
    # shg()

    xv = M[[0, 3, 3, 0, 0, NaN, 1, 1, 2, 2, 1]]
    yv = M[[0, 0, 3, 3, 0, NaN, 1, 2, 2, 1, 1]]
    x = rand(1000, 1) * 3
    y = rand(1000, 1) * 3
    _in = inpolygon(x, y, xv, yv)
    plot(xv, yv, x(_in), y(_in), ".r", x(_not(_in)), y(_not(_in)), ".b")
    # shg()

    # # for plot inside matlab
    # disp("")
    # disp(f'xv = [{" ".join(xv.astype(str).reshape(-1).tolist())}]')
    # disp(f'yv = [{" ".join(yv.astype(str).reshape(-1).tolist())}]')
    # disp(f'x = [{" ".join(x.astype(str).reshape(-1).tolist())}]')
    # disp(f'y = [{" ".join(y.astype(str).reshape(-1).tolist())}]')
    # disp(f'in = 1==[{" ".join(_in.astype(int).astype(str).reshape(-1).tolist())}]')
    # disp("plot(xv,yv,x(in),y(in),'.r',x(~in),y(~in),'.b')")


def test_inpolygon2():
    P = M[[(pi * 1) / 4, (pi * 3) / 4, (pi * 5) / 4, (pi * 7) / 4, (pi * 1) / 4]]
    L = M[
        [
            (pi * 1) / 4,
            (pi * 3) / 4,
            (pi * 5) / 4,
            (pi * 7) / 4,
            (pi * 1) / 4,
            nan,
            0,
            1.25663706143592,
            2.51327412287183,
            3.76991118430775,
            5.02654824574367,
            6.28318530717959,
        ]
    ]
    xvp = cos(P).H
    yvp = sin(P).H
    xv = cos(L).H
    yv = sin(L).H
    xq = M[[0.5377, 1.8339, -2.2588, 0.8622, 0.3188, -1.3077, -0.4336, 0, 1, 2.7694]]
    yq = M[
        [
            -0.8637,
            0.0774,
            -1.2141,
            -1.1135,
            -0.0068,
            1.5326,
            -0.7697,
            sin(pi / 4),
            0,
            1.1174,
        ]
    ]
    inp, onp = inpolygon(xq, yq, xvp, yvp)
    _assert(
        isequal(inp, M[[0, 0, 0, 0, 1, 0, 0, 1, 0, 0]]),
        "inpolygon fails for parameters inside pentagon",
    )
    _assert(
        isequal(onp, M[[0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]),
        "inpolygon fails for parameters on pentagon",
    )
    _in, on = inpolygon(xq, yq, xv, yv)
    _assert(
        isequal(_in, M[[0, 0, 0, 0, 1, 0, 0, 1, 1, 0]]),
        "inpolygon fails for parameters inside intersecting pentagon and rectangle",
    )
    _assert(
        isequal(on, M[[0, 0, 0, 0, 0, 0, 0, 1, 1, 0]]),
        "inpolygon fails for parameters on intersecting pentagon and rectangle",
    )

    plot(
        xv,
        yv,
        "k:",
        xq(_in),
        yq(_in),
        "bo",
        xq(on),
        yq(on),
        "r.",
        xq(_not(_in)),
        yq(_not(_in)),
        "m+",
    )
    # shg()


if __name__ == "__main__":
    test_inpolygon()
