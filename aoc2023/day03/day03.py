# day03.py
import os


class SearchBlock:
    top: str
    current: str
    bottom: str
    num: str
    start: int

    def __init__(self):
        self.top = self.current = self.bottom = ''

    def process_current(self):
        # find all the numbers (not just digits) in the current line and for each
        # determine if it has an adjacent symbol. add number to a sum for the current line
        # and return it
        self.num = ''
        self.start = 0
        line_sum = 0
        for i, c in enumerate(self.current):
            if c.isdigit():
                if len(self.num) == 0:
                    # position of first digit for a new number
                    self.start = i
                self.num += c
            else:
                # check if we've come to the end of the number
                if len(self.num) > 0:
                    print('numeric detected', self.num, 'at start', self.start)
                    # now do something with the number
                    if self.search_symbol():
                        line_sum += int(self.num)
                    self.num = ''
        return line_sum

    def search_symbol(self):
        # todo search top, current, bottom for a 1 char border for a non-digit or period
        return True


def test_part_one():
    block = SearchBlock()
    sum_of_part_numbers = 0
    with open(os.path.join(os.path.dirname(__file__), 'day03_test.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            block.bottom = a_line.strip()
            if len(block.current) == 0:
                # if on the first line of input, initialise top and current with periods
                # so first run of process_current() isn't dealing with an empty string
                block.top = block.current = '.' * len(block.bottom)
            sum_of_part_numbers += block.process_current()

            # shift up ready for next loop
            block.top = block.current
            block.current = block.bottom

        # one more iteration at eof. fill bottom with periods for the same reason we filled
        # top & current right at the start
        block.bottom = '.' * len(block.bottom)
        sum_of_part_numbers += block.process_current()

    print(sum_of_part_numbers)
    return sum_of_part_numbers
