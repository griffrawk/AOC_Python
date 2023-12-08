# day03.py
import os
import re


# Redundant for the moment
class SearchBlock:
    def __init__(self):
        self.top = self.current = self.bottom = ''

    def potential_ratio(self, i):
        # we have a number in current. we saw a '*' so we find another number by '*'
        # trouble is, the '*' may be in top or bottom and if so the number may be in
        # the line above top or below bottom
        # does that mean we put in a 5 line buffer?
        # i'm convinced as always I'm over-complicating this.
        pass

    def wont_work_potential_ratio(self, i):

        # Look around the * to find numbers
        potential_top = potential_left = potential_right = potential_bottom = ''
        z = 0
        # TODO I'm aiming for some sort of loop that starting from i, makes two more position
        #   l (going backwards & r (going forwards), both limited ofc. top, current and bottom are
        #   then sampled at l & r and if a digit is found
        #   then it is either prepended or appended to a potential string. Loop ends when all 4
        #   sampling points return a non-digit at their position.
        #   z == 0 is ignored for current, as that is the '*'. Similarly z == 0 for top and bottom
        #   is also allowed to have a non-digit and not terminate the loop, as the number in top & bottom
        #   may be on a diagonal from '*'
        #   Resurrect this approach. Instead of trying to be clever and find 4 potentials simultaneously
        #   do each one individually, as otherwise it gets messed up. Have to be clever where a number is
        #   directly above '*' though...
        #   Need to see if I can reuse some code. I've already go a scanner (for part 1) but need to factor
        #   it into a more general function, and also deal with going backwards
        while True:
            # TODO this doesn't deal with reaching the end of a line in either direction while still
            #   being valid in the other direction
            l = max(i - z, 0)
            r = min(i + z, len(self.current))
            top_l = self.top[l]
            top_r = self.top[r]
            current_l = self.current[l]
            current_r = self.current[r]
            bottom_l = self.bottom[l]
            bottom_r = self.bottom[r]
            if z > 0:
                if top_l.isdigit() \
                        and top_r.isdigit() \
                        and current_l.isdigit() \
                        and current_r.isdigit() \
                        and bottom_l.isdigit() \
                        and bottom_r.isdigit():
                    break
            # if each sampled character isdigit, then prepend or append to top & bottom
            # or make separate left & right candidates
            if top_l.isdigit():
                potential_top = top_l + potential_top
            if top_r.isdigit():
                potential_top = potential_top + top_r
            if current_l.isdigit():
                potential_left = current_l + potential_left
            if current_r.isdigit():
                potential_right = potential_right + top_r
            if bottom_l.isdigit():
                potential_bottom = bottom_l + potential_bottom
            if top_r.isdigit():
                potential_bottom = potential_bottom + bottom_r

            z += 1
        print('potential_top\t', potential_top)
        print('potential_left\t', potential_left)
        print('potential_right\t', potential_right)
        print('potential_bottom\t', potential_bottom)

        pass

        self.ratio_sum = 0

    def process_current_old(self):
        # Deprecated in favour of regexp version

        # Find all the numbers in the current line and for each determine if it has an adjacent
        # symbol. Add number to a sum for the current line and return it.
        # If * is noticed along the way, do a lookaround for at least two gear values to cal ratio.
        self.num_str = ''
        self.start = 0
        self.part_sum = 0
        self.ratio_sum = 0

        for i, c in enumerate(self.current):
            if c == '*':
                self.potential_ratio(i)
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


def part_one():
    top = current = bottom = ''
    sum_of_part_sum = 0

    def process_current():
        # Find all the numbers in the current line and for each determine if it has an adjacent
        # symbol. Add number to a sum for the current line and return it.
        part_sum = 0
        nonlocal top, current, bottom
        for match in re.finditer(r"\d+", current):
            num_str = match.group(0)
            border_left = max(match.start() - 1, 0)
            border_right = match.end() + 1
            surroundings = (top[border_left:border_right] + current[border_left:border_right]
                      + bottom[border_left:border_right])
            if len(''.join(filter(lambda x: not (x.isdigit() or x == '.'), surroundings))) > 0:
                part_sum += int(num_str)
        return part_sum

    with (open(os.path.join(os.path.dirname(__file__), 'day03_data.txt'), 'r', encoding='utf-8') as a_file):
        for a_line in a_file:
            bottom = a_line.strip()
            if len(current) == 0:
                # If on the first line of input, initialise top and current with periods
                # so first run of process_current() isn't dealing with an empty string
                top = current = '.' * len(bottom)
            sum_of_part_sum += process_current()

            # shift up ready for next loop
            top = current
            current = bottom

        # One more iteration at EOF. Fill bottom with periods for the same reason we filled
        # top & current right at the start
        bottom = '.' * len(bottom)
        sum_of_part_sum += process_current()

    print(sum_of_part_sum)
    return sum_of_part_sum
