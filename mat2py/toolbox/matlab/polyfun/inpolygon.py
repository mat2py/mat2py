# type: ignore

import mat2py as mp
from mat2py.core import *


def inpolygon(x, y, xv, yv, nargout=None):
    _in, on = (None,) * 2

    if (_not(isvector(xv))) or (_not(isvector(yv))):
        error(message("MATLAB:inpolygon:PolygonVecDef"))
    xv = xv[I[:]]
    yv = yv[I[:]]
    inputSize = size(x)
    x = x[I[:]].T
    y = y[I[:]].T
    mask = (((x >= min(xv)) & (x <= max(xv))) & (y >= min(yv))) & (y <= max(yv))
    if _not(any(mask)):
        _in = zeros(inputSize) != 0
        on = copy(_in)
        return (_in, on)[:nargout]
    xv, yv = close_loops(xv, yv)
    Nv = length(xv)
    xrange = max(xv) - min(xv)
    yrange = max(yv) - min(yv)
    min_safe_limit = 1.0e-15
    max_safe_limit = 1.0e150
    if (xrange < min_safe_limit) or (yrange < min_safe_limit):
        warning(message("MATLAB:inpolygon:ModelingWorldLower"))
    if (xrange > max_safe_limit) or (yrange > max_safe_limit):
        warning(message("MATLAB:inpolygon:ModelingWorldUpper"))
    inbounds = find(mask)
    x = x(mask)
    y = y(mask)
    block_length = 1e5
    _M = numel(x)
    if (M[_M] @ Nv) < block_length:
        if nargout > 1:
            _in, on = vec_inpolygon(Nv, x, y, xv, yv)
        else:
            _in, _ = vec_inpolygon(Nv, x, y, xv, yv)
    else:
        N = ceil(mrdivide(block_length, Nv))
        _in = zeros(1, _M) != 0
        if nargout > 1:
            on = zeros(1, _M) != 0
        n2 = 0
        while n2 < _M:
            n1 = n2 + 1
            n2 = n1 + N
            if n2 > _M:
                n2 = copy(_M)
            if nargout > 1:
                _in[I[n1:n2]], on[I[n1:n2]] = vec_inpolygon(
                    Nv, x(M[n1:n2]), y(M[n1:n2]), xv, yv
                )
            else:
                _in[I[n1:n2]] = vec_inpolygon(Nv, x(M[n1:n2]), y(M[n1:n2]), xv, yv)

    if nargout > 1:
        onmask = copy(mask)
        onmask[I[inbounds(_not(on))]] = 0
        on = reshape(onmask, inputSize)
    mask[I[inbounds(_not(_in))]] = 0
    _in = reshape(mask, inputSize)
    return (_in, on)[:nargout]


def vec_inpolygon(Nv, x, y, xv, yv):
    Np = length(x)
    x = x[I[ones(Nv, 1), :]]
    y = y[I[ones(Nv, 1), :]]
    m = M[1 : (Nv - 1)]
    mp1 = M[2:Nv]
    avx = abs(0.5 * (xv[I[m, :]] + xv[I[mp1, :]]))
    avy = abs(0.5 * (yv[I[m, :]] + yv[I[mp1, :]]))
    scaleFactor = max(avx(m), avy(m))
    scaleFactor = max(scaleFactor, avx[I[m, :]] * avy[I[m, :]])
    xv = xv[I[:, ones(1, Np)]] - x
    yv = yv[I[:, ones(1, Np)]] - y
    posX = xv > 0
    posY = yv > 0
    negX = _not(posX)
    negY = _not(posY)
    quad = ((negX & posY) + (2.0 * (negX & negY))) + (3 * (posX & negY))
    nanidx = isnan(xv) | isnan(yv)
    quad[I[nanidx]] = copy(NaN)
    theCrossProd = (xv[I[m, :]] * yv[I[mp1, :]]) - (xv[I[mp1, :]] * yv[I[m, :]])
    signCrossProduct = sign(theCrossProd)
    scaledEps = (scaleFactor @ M[eps]) * 3
    idx = bsxfun(lt, abs(theCrossProd), scaledEps)
    signCrossProduct[I[idx]] = 0
    dotProduct = (xv[I[m, :]] * xv[I[mp1, :]]) + (yv[I[m, :]] * yv[I[mp1, :]])
    diffQuad = diff(quad)
    idx = abs(diffQuad) == 3
    diffQuad[I[idx]] = (-diffQuad(idx)) / 3
    idx = abs(diffQuad) == 2
    diffQuad[I[idx]] = 2 * signCrossProduct(idx)
    nanidx = isnan(diffQuad)
    diffQuad[I[nanidx]] = 0
    _in = sum(diffQuad) != 0
    on = any((signCrossProduct == 0) & (dotProduct <= 0))
    _in = _in | on
    return _in, on


def close_loops(xv, yv):
    xnan = isnan(xv)
    ynan = isnan(yv)
    if _not(any(xnan | ynan)):
        nump = length(xv)
        if nump < 3:
            return
        if (xv(1) != xv(nump)) or (yv(1) != yv(nump)):
            xv = M[
                xv,
                xv(1),
            ]
            yv = M[
                yv,
                yv(1),
            ]
    else:
        if any(xnan != ynan):
            error(message("MATLAB:inpolygon:InvalidLoopDef"))
        xnanShift = M[
            true,
            xnan[I[1 : (end - 1)]],
        ]
        redundantNaN = xnan & xnanShift
        xv = xv(_not(redundantNaN))
        yv = yv(_not(redundantNaN))
        if _not(isnan(xv[I[end]])):
            xv = M[
                xv,
                NaN,
            ]
            yv = M[
                yv,
                NaN,
            ]
        nanLoc = find(isnan(xv))
        startIdx = 1
        growBy = 0
        numLoops = length(nanLoc)
        for l in M[1:numLoops]:
            endIdx = nanLoc(l) - 1
            loopclosed = (xv(startIdx) == xv(endIdx)) and (yv(startIdx) == yv(endIdx))
            if _not(loopclosed):
                growBy = growBy + 1
            startIdx = endIdx + 2

        xv = xv[I[1 : (end - 1)]]
        yv = yv[I[1 : (end - 1)]]
        if growBy > 0:
            xvnew = zeros(length(xv) + growBy, 1)
            yvnew = zeros(length(xv) + growBy, 1)
            startIdx = 1
            idxOffset = 0
            for l in M[1:numLoops]:
                endIdx = nanLoc(l) - 1
                xvnew[I[idxOffset + (M[startIdx:endIdx])]] = xv(M[startIdx:endIdx])
                yvnew[I[idxOffset + (M[startIdx:endIdx])]] = yv(M[startIdx:endIdx])
                loopclosed = (xv(startIdx) == xv(endIdx)) and (
                    yv(startIdx) == yv(endIdx)
                )
                if _not(loopclosed):
                    idxOffset = idxOffset + 1
                    xvnew[I[idxOffset + endIdx]] = xv(startIdx)
                    yvnew[I[idxOffset + endIdx]] = yv(startIdx)
                if ((idxOffset + endIdx) + 1) > size(xvnew, 1):
                    xvnew = M[
                        xvnew,
                        zeros(((idxOffset + endIdx) + 1) - size(xvnew, 1), 1),
                    ]
                    yvnew = M[
                        yvnew,
                        zeros(((idxOffset + endIdx) + 1) - size(yvnew, 1), 1),
                    ]
                xvnew[I[(idxOffset + endIdx) + 1]] = copy(NaN)
                yvnew[I[(idxOffset + endIdx) + 1]] = copy(NaN)
                startIdx = endIdx + 2

            xv = copy(xvnew)
            yv = copy(yvnew)
    return xv, yv
