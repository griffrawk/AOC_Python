# day08.py
import os
from collections import deque
# import re


def part_one(file):
    route = {}
    with open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            if '=' in a_line:
                pos, branch = a_line.split('=')
                left, right = branch.strip(' ()').split(',')
                route[pos.strip()] = (left.strip(), right.strip())
        a_file.seek(0)
        directions = deque([x for x in a_file.readline().strip()])

    count = 0
    pos = 'AAA'
    while True:
        match directions[0]:
            case 'L':
                pos = route[pos][0]
            case 'R':
                pos = route[pos][1]
        count += 1
        if pos == 'ZZZ':
            break
        directions.rotate(-1)

    print(count)
    return count
