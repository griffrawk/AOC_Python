# day001.py
# --- Day 1: Trebuchet?! ---
# filter input for numbers, pick first and last number (may be the same),
# data = first * 10 + second
# sum up data


import os


def part_one():
    sumup = 0
    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            digits = ''.join(filter(str.isdigit, a_line))
            if len(digits) > 0:
                sumup += int(digits[0:1] + digits[-1])
    return sumup



def part_two():
    count = 0
    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            pass
    return count
