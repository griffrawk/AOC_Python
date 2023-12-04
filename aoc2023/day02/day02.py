# day02.py
import os


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
def part_one():
    limits = {'red': 12, 'green': 13, 'blue': 14}
    sum_up = 0
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

# def part_two():
#     sumup = 0
#     numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     with open(os.path.join(os.path.dirname(__file__), 'day01_data.txt'), 'r', encoding='utf-8') as a_file:
#         for a_line in a_file:
#             # replace the word with corresponding number, but sandwich number in words
#             # this is to catch cases like 'oneight' where one word flows into another
#             # so produces 'one1oneight8eight'. this should catch all cases regardless of number replace order
#             # work on a copy just in case
#             a_copy = copy.copy(a_line)
#             for n in range(10):
#                 a_copy = a_copy.replace(numbers[n], numbers[n] + str(n) + numbers[n])
#             # print(a_copy)
#             digits = ''.join(filter(str.isdigit, a_copy))
#             if len(digits) > 0:
#                 sumup += int(digits[0:1] + digits[-1])
#     print(sumup)
#     return sumup
