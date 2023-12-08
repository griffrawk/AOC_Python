# day03.py
import os
import re


def process_part(top, current, bottom):
    # Find all the numbers in the current line and for each determine if it has an adjacent
    # symbol. Add number to a sum for the current line and return it.
    part_sum = 0
    for match in re.finditer(r"\d+", current):
        num_str = match.group(0)
        border_left = max(match.start() - 1, 0)
        # border_right can exceed the length of line, as Python's forgiving like that...!
        border_right = match.end() + 1
        surroundings = (top[border_left:border_right] + current[border_left:border_right]
                        + bottom[border_left:border_right])
        if len(''.join(filter(lambda x: not (x.isdigit() or x == '.'), surroundings))) > 0:
            part_sum += int(num_str)
    return part_sum


def process_ratio(top, current, bottom):
    # Look for ratio symbols '*' in current, then look for numbers in top, current, bottom,
    # and check how near each is to the ratio symbol. They must touch horizontally, vertically, diagonally.
    # Create a list and then at the end of examining each '*', calclulate the product and sum for current.
    # Return to be further summed for whole file.
    ratio_prod_sum = 0

    # Differences for the start & end checks
    ends = [-1, 0]
    starts = [0, 1]

    numbers = re.compile(r"\d+")

    for ratios in re.finditer(r"\*", current):
        # A list of numbers adjacent to '*'
        gears = []
        ratio_pos = ratios.start()

        # The iterators need redoing each pass unfortunately (could do them earlier and stick in a list of tuples...)
        top_gears = numbers.finditer(top)
        current_gears = numbers.finditer(current)
        bottom_gears = numbers.finditer(bottom)

        for potential_gears in top_gears, current_gears, bottom_gears:
            for potential_gear in potential_gears:
                # Check adjacency of potential gear to ratio symbol, then it's a gear and not just a number
                if potential_gear.start() - ratio_pos in starts or \
                        potential_gear.end() - ratio_pos - 1 in ends or \
                        potential_gear.start() < ratio_pos < potential_gear.end() - 1:
                    gears.append(potential_gear.group(0))
        # Multiply ratios (should be more than 1 gear)
        # print('gears',gears)
        ratio_prod = 0
        if len(gears) > 1:
            ratio_prod = 1
            for gear in gears:
                ratio_prod *= int(gear)
        # print('prod', ratio_prod)
        ratio_prod_sum += ratio_prod

    return ratio_prod_sum


def part_one_two():
    top = current = bottom = ''
    sum_of_part_sum = 0
    sum_of_ratio_prod = 0
    with (open(os.path.join(os.path.dirname(__file__), 'day03_data.txt'), 'r', encoding='utf-8') as a_file):
        for a_line in a_file:
            bottom = a_line.strip()
            if len(current) == 0:
                # If on the first line of input, initialise top and current with periods
                # so first run of process_current() isn't dealing with an empty string
                top = current = '.' * len(bottom)
            sum_of_part_sum += process_part(top, current, bottom)
            sum_of_ratio_prod += process_ratio(top, current, bottom)

            # shift up ready for next loop
            top = current
            current = bottom

        # One more iteration at EOF. Move last line of file in bottom up to current
        # Fill bottom with periods for the same reason we filled
        # top & current right at the start
        bottom = '.' * len(bottom)
        sum_of_part_sum += process_part(top, current, bottom)
        sum_of_ratio_prod += process_ratio(top, current, bottom)

    print(sum_of_part_sum, sum_of_ratio_prod)
    return sum_of_part_sum, sum_of_ratio_prod
