# day02.py
import os
from math import prod


class Continue(Exception):
    pass


# Use an exception to break to the outer loop. 'Some' might say it abuses exceptions.
# In addition, if I had more than one set of nested loops to break from, I'd need to setup
# more than one exception class possibly, or does it know to use the correct `except:`?
# That would start to get messy.
def part_one_alt():
    limits = {'red': 12, 'green': 13, 'blue': 14}
    sum_up = 0
    with open(os.path.join(os.path.dirname(__file__), 'day02_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            game, hands = a_line.split(':')
            try:
                for hand in hands.split(';'):
                    for cube in hand.split(','):
                        count, colour = cube.split()
                        if int(count) > limits[colour]:
                            # break out of hands loop, the whole game is invalid
                            raise Continue
            except Continue:
                continue
            # add game number to sum
            sum_up += int(game.split()[1])

    print(sum_up)
    return sum_up


# 'Some' argue the inner function way of breaking to an outer loop is preferable, or extracting
# inner function to a separate top-level, if too unwieldy. But a separate func would need params,
# as it loses scope of the top-level vars. eg to pass `hands`
# On reflection I like it this way, for this use at least! The game check inner func can be
# treated as a condition. Clearer to see what it's doing.
# https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops
# https://stackoverflow.com/questions/189645/how-can-i-break-out-of-multiple-loops
def part_one():
    limits = {'red': 12, 'green': 13, 'blue': 14}
    sum_up = sum_powers = 0
    with open(os.path.join(os.path.dirname(__file__), 'day02_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            game, hands = a_line.split(':')

            def valid_game():
                for hand in hands.split(';'):
                    for cube in hand.split(','):
                        count, colour = cube.split()
                        if int(count) > limits[colour]:
                            # break out of hands loop, the whole game is invalid
                            return False
                return True

            # add game number to sum
            if valid_game():
                sum_up += int(game.split()[1])

    print(sum_up)
    return sum_up


# Now find the sum of the powers of the maximum of each cube colour count. Combined it with the part_one
# solution, but now the loop examines every hand in every game. No early loop termination, but check game
# validity with a flag.
def part_one_two():
    sum_up = sum_maxima = 0
    limits = {'red': 12, 'green': 13, 'blue': 14}
    with open(os.path.join(os.path.dirname(__file__), 'day02_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            game, hands = a_line.split(':')
            maxima = {}
            valid_game = True
            for hand in hands.split(';'):
                for cube in hand.split(','):
                    count, colour = cube.split()
                    if int(count) > limits[colour]:
                        valid_game = False
                    maxima[colour] = max(maxima.get(colour, 0), int(count))

            if valid_game:
                sum_up += int(game.split()[1])

            sum_maxima += prod(maxima.values())

    print(sum_up, sum_maxima)
    return sum_up, sum_maxima
