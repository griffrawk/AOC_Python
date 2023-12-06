# day03.py
import os


class SearchBlock:
    def __init__(self):
        self.num_str = self.top = self.current = self.bottom = ''
        self.part_sum = self.ratio_sum = self.start = 0

    def potential_number(self):
        # Check if we've come to the end of the number and not just come to the end
        # of current without detecting any numbers
        if len(self.num_str) > 0:
            # Now do something with the number
            if self.search_symbol():
                self.part_sum += int(self.num_str)
            # Init ready for next number
            self.num_str = ''

    def potential_ratio(self):
        # Look around the * to find numbers
        potential_top = potential_left = potential_right = potential_bottom = ''
        z = 0
        # while True:
        #     if self.top[i - z].isdigit() \
        #         or self.top[i + z].isdigit() \
        #             or self.current[i - z].isdigit() \
        #             or self.current[i + z].isdigit() \
        #             or self.bottom[i - z].isdigit() \
        #             or self.bottom[i + z].isdigit():
        #         pass
        #     pass
        self.ratio_sum += 0

    def process_current(self):
        # Find all the numbers in the current line and for each determine if it has an adjacent
        # symbol. Add number to a sum for the current line and return it.
        # If * is noticed along the way, do a lookaround for at least two gear values to cal ratio.
        self.num_str = ''
        self.start = 0
        self.part_sum = 0
        self.ratio_sum = 0

        for i, c in enumerate(self.current):
            if c == '*':
                self.potential_ratio()
            if c.isdigit():
                if len(self.num_str) == 0:
                    # Position of first digit for a new number
                    self.start = i
                # Build the number
                self.num_str += c
            else:
                self.potential_number()
        # Catch possible last number at end of current
        self.potential_number()
        return self.part_sum, self.ratio_sum

    def search_symbol(self):
        border_left = max(self.start - 1, 0)
        border_right = self.start + len(self.num_str) + 1
        search = (self.top[border_left:border_right] + self.current[border_left:border_right]
                  + self.bottom[border_left:border_right])
        # print(search)
        if len(''.join(filter(lambda x: not(x.isdigit() or x == '.'), search))) > 0:
            return True
        return False


def part_one_two():
    block = SearchBlock()
    sum_of_part_sum = sum_of_ratio_sum = 0

    def process_current():
        nonlocal sum_of_part_sum, sum_of_ratio_sum
        parts, ratios = block.process_current()
        sum_of_part_sum += parts
        sum_of_ratio_sum += ratios

    with (open(os.path.join(os.path.dirname(__file__), 'day03_data.txt'), 'r', encoding='utf-8') as a_file):
        for a_line in a_file:
            block.bottom = a_line.strip()
            if len(block.current) == 0:
                # If on the first line of input, initialise top and current with periods
                # so first run of process_current() isn't dealing with an empty string
                block.top = block.current = '.' * len(block.bottom)
            process_current()

            # shift up ready for next loop
            block.top = block.current
            block.current = block.bottom

        # One more iteration at EOF. Fill bottom with periods for the same reason we filled
        # top & current right at the start
        block.bottom = '.' * len(block.bottom)
        process_current()

    print(sum_of_part_sum, sum_of_ratio_sum)
    return sum_of_part_sum, sum_of_ratio_sum
