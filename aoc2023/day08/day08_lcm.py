# day08.py
import os
from collections import deque
from math import lcm
import copy


def part_two(file):
    route = {}
    starts = []
    counts = []
    with open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            if '=' in a_line:
                pos, branch = a_line.split('=')
                pos = pos.strip()
                left, right = branch.strip(' ()').split(',')
                route[pos] = (left.strip(), right.strip())
                if pos[-1] == 'A':
                    starts.append(pos)
        a_file.seek(0)
        directions = deque([x for x in a_file.readline().strip()])

    for pos in starts:
        # Reset the directions
        dirs = copy.copy(directions)
        count = 0
        while True:
            match dirs[0]:
                case 'L':
                    pos = route[pos][0]
                case 'R':
                    pos = route[pos][1]
            count += 1
            if pos[-1] == 'Z':
                break
            dirs.rotate(-1)
        counts.append(count)

    multiple = lcm(*tuple(counts))
    print(counts, multiple)
    return multiple
