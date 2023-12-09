# day02.py
import os
from math import prod


def test_part_one():
    sum_up = 0
    with open(os.path.join(os.path.dirname(__file__), 'day04_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            left, right = a_line.split(':')[1].split('|')
            winning = set([x for x in left.split()])
            draw = set([x for x in right.split()])
            if (power := len(winning.intersection(draw)) - 1) >= 0:
                sum_up += 2 ** power
    print(sum_up)
    return sum_up
