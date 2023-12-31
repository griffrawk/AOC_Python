import os
import math
import copy
import re


def part_one(file):
    sum_up = 0
    with open( os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            seq = [int(x) for x in re.findall(r"-*\d+", a_line)]
            sum_up += gregory_newton(seq, len(seq))
    print(sum_up)
    return sum_up


def gregory_newton(fx, i):
    derivatives = []
    t = copy.copy(fx)
    while True:
        dx = [t[i + 1] - t[i] for i in range(0, len(t) - 1)]
        if dx.count(0) == len(dx):
            break
        else:
            derivatives.append(dx[0])
            t = copy.copy(dx)
    # First term
    n = fx[0]
    for p, dx in enumerate(derivatives, start=1):
        # Sum first term of each derivative * binomial coefficient
        n += dx * math.comb(i, p)
    return n


def test_gregory_newton():
    fx = [10, 13, 16, 21, 30, 45]
    # Calc the next ones
    assert gregory_newton(fx, 6) == 68
    assert gregory_newton(fx, 7) == 101

    fx = [7, 15, 32, 57, 98, 176, 332, 653, 1352, 2972, 6842, 16010,
          37046, 83402, 181521, 381725, 777249, 1536841, 2959392,
          5563435, 10230470]
    # Calc the next one
    assert gregory_newton(fx, 21) == 18429424

    fx = [16, 33, 50, 64, 72, 76, 90, 143, 264, 419, 340, -868, -5538,
          -18941, -51661, -122356, -258160, -484127, -779910, -954772, -340276]
    # Sanity check existing seq members
    assert gregory_newton(fx, 9) == 419
    assert gregory_newton(fx, 11) == -868
    # Calc the next one
    assert gregory_newton(fx, 21) == 2893370
