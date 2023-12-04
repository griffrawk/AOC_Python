# day001.py
# --- Day 1: Trebuchet?! ---
# filter input for numbers, pick first and last number (may be the same),
# data = first * 10 + second
# sum up data


import os, copy


def part_one():
    sumup = 0
    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            digits = ''.join(filter(str.isdigit, a_line))
            if len(digits) > 0:
                sumup += int(digits[0:1] + digits[-1])
    print(sumup)
    return sumup



def part_two():
    sumup = 0
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            # replace the word with corresponding number, but sandwich number in words
            # this is to catch cases like 'oneight' where one word flows into another
            # so produces 'one1oneight8eight'. this should catch all cases regardless of number replace order
            # work on a copy just in case
            a_copy = copy.copy(a_line)
            for n in range(10):
                a_copy = a_copy.replace(numbers[n], numbers[n] + str(n) + numbers[n])
            # print(a_copy)
            digits = ''.join(filter(str.isdigit, a_copy))
            if len(digits) > 0:
                sumup += int(digits[0:1] + digits[-1])
    print(sumup)
    return sumup

