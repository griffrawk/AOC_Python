# day08_longwinded.py
# this won't work in any short time

import os
from collections import deque
from bitarray import bitarray


def part_one_two(file, part_two=False):
    route = {}
    starts = []
    complete = bitarray()

    with open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            if '=' in a_line:
                pos, branch = a_line.split('=')
                pos = pos.strip()
                left, right = branch.strip(' ()').split(',')
                route[pos] = (left.strip(), right.strip())
                if part_two:
                    if pos[-1] == 'A':
                        starts.append(pos)
                        complete.append(0)
        a_file.seek(0)
        directions = deque([x for x in a_file.readline().strip()])

    if not part_two:
        starts.append('AAA')
        complete.append(0)

    print(starts)
    count = 1
    while True:
        for idx, pos in enumerate(starts):
            match directions[0]:
                case 'L':
                    pos = route[pos][0]
                case 'R':
                    pos = route[pos][1]
            if pos[-1] == 'Z':
                complete[idx] = 1
            else:
                complete[idx] = 0
            starts[idx] = pos
        if complete.all():
            break

        count += 1
        directions.rotate(-1)

        if count % 1000000 == 0:
            print(count, complete)

    print(count, complete)
    return count
