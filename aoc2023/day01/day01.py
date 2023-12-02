# day001.py
# --- Day 1: Trebuchet?! ---
# filter input for numbers, pick first and last number (may be the same),
# data = first * 10 + second
# sum up data


import os


def part_one():
    previous = 0
    count = 0
    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            current = int(a_line.rstrip())
            if current > previous != 0:
                count += 1
            previous = current
    print('Depth measurement increases {} times'.format(count))
    return count


def part_two():
    previous = 0
    count = 0
    input_count = 0
    d_0 = d_1 = d_2 = 0

    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            input_count += 1
            # move the window along
            d_2 = d_1
            d_1 = d_0
            d_0 = int(a_line.rstrip())
            current = d_2 + d_1 + d_0
            # wait until at least 3 datapoints have been read
            if current > previous != 0 and input_count > 3:
                count += 1
            previous = current
    print('Depth measurement increases {} times, in a 3 measurement sliding window'.format(count))
    return count
