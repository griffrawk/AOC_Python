# day03.py
import os


class SearchBlock:
    top: str
    current: str
    bottom: str

    def __init__(self):
        self.top = self.current = self.bottom = ''

    def process_current(self):
        # Find all the numbers in the current line and for each
        # determine if it has an adjacent symbol. Add number to a sum for the current line
        # and return it.
        num_str = ''
        start = 0
        line_sum = 0

        def do_something():
            # Check if we've come to the end of the number and not just come to the end
            # of current without detecting any numbers
            nonlocal num_str, line_sum, start
            if len(num_str) > 0:
                # Now do something with the number
                if self.search_symbol(num_str, start):
                    line_sum += int(num_str)
                # Init ready for next number
                num_str = ''

        for i, c in enumerate(self.current):
            if c.isdigit():
                if len(num_str) == 0:
                    # Position of first digit for a new number
                    start = i
                # Build the number
                num_str += c
            else:
                do_something()
        # last number at end of current
        do_something()
        return line_sum

    def search_symbol(self, num_str: str, start: int):
        border_left = max(start - 1, 0)
        border_right = start + len(num_str) + 1
        search = (self.top[border_left:border_right] + self.current[border_left:border_right]
                  + self.bottom[border_left:border_right])
        # print(search)
        if len(''.join(filter(lambda x: not(x.isdigit() or x == '.'), search))) > 0:
            return True

        return False


def test_part_one():
    block = SearchBlock()
    sum_of_part_numbers = 0
    with open(os.path.join(os.path.dirname(__file__), 'day03_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            block.bottom = a_line.strip()
            if len(block.current) == 0:
                # If on the first line of input, initialise top and current with periods
                # so first run of process_current() isn't dealing with an empty string
                block.top = block.current = '.' * len(block.bottom)
            sum_of_part_numbers += block.process_current()

            # shift up ready for next loop
            block.top = block.current
            block.current = block.bottom

        # One more iteration at eof. Fill bottom with periods for the same reason we filled
        # top & current right at the start
        block.bottom = '.' * len(block.bottom)
        sum_of_part_numbers += block.process_current()

    print(sum_of_part_numbers)
    return sum_of_part_numbers
