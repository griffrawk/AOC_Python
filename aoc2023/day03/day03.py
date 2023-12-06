# day03.py
import os


class SearchBlock:
    top: str
    current: str
    bottom: str
    numstr: str
    start: int

    def __init__(self):
        self.top = self.current = self.bottom = ''

    def process_current(self):
        # Find all the numbers in the current line and for each
        # determine if it has an adjacent symbol. Add number to a sum for the current line
        # and return it.
        self.numstr = ''
        self.start = 0
        line_sum = 0
        for i, c in enumerate(self.current):
            if c.isdigit():
                if len(self.numstr) == 0:
                    # Position of first digit for a new number
                    self.start = i
                self.numstr += c
            else:
                # Check if we've come to the end of the number and not just come to the end
                # of current without detecting any numbers
                if len(self.numstr) > 0:
                    # print('numeric detected', self.numstr, 'at start', self.start)
                    # Now do something with the number
                    if self.search_symbol():
                        line_sum += int(self.numstr)
                    # Init ready for next number
                    self.numstr = ''
        return line_sum

    def search_symbol(self):
        # TODO Search top, current, bottom for a 1 char border for a non-digit or period and return True
        return True


def test_part_one():
    block = SearchBlock()
    sum_of_part_numbers = 0
    with open(os.path.join(os.path.dirname(__file__), 'day03_test.txt'), 'r', encoding='utf-8') as a_file:
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
