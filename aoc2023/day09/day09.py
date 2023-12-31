import math
import copy


def test_gregory_newton():
    x = [10, 13, 16, 21, 30, 45]
    assert gregory_newton(x, 6) == 68
    assert gregory_newton(x, 7) == 101


def gregory_newton(x, i):
    d = []
    t = copy.copy(x)
    while True:
        dx = [t[i + 1] - t[i] for i in range(0, len(t) - 1)]
        if dx.count(0) == len(dx):
            break
        else:
            d.append(dx)
            t = copy.copy(dx)
    n = x[0]
    for p, dx in enumerate(d):
        n += dx[0] * math.comb(i, p + 1)
    return n
