import os


def part_one():
    horiz = depth = 0

    with open(os.path.join(os.path.dirname(__file__), 'day02_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            (action, amount) = a_line.rstrip().split(' ')
            amount = int(amount)
            if action == 'forward':
                horiz = horiz + amount
            elif action == 'up':
                depth = depth - amount
            elif action == 'down':
                depth = depth + amount
    print('Final position multiple = {}'.format(horiz * depth))
    return horiz * depth


def part_two():
    aim = horiz = depth = 0

    with open(os.path.join(os.path.dirname(__file__), 'day02_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            (action, amount) = a_line.rstrip().split(' ')
            amount = int(amount)
            if action == 'forward':
                horiz += amount
                depth += aim * amount
            elif action == 'up':
                aim -= amount
            elif action == 'down':
                aim += amount
            # print('{}, horiz = {}, aim = {}, depth = {}'.format(vector, horiz, aim, depth))

    print('Final position multiple = {}'.format(horiz * depth))
    assert horiz * depth == 2086261056
