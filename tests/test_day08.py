from aoc2023.day08.day08 import part_one
from aoc2023.day08.day08_lcm import part_two


def test_part_one():
    assert part_one('day08_part_one_test_1.txt') == 2
    assert part_one('day08_part_one_test_2.txt') == 6
    assert part_one('day08_data.txt') == 11911


def test_part_two():
    assert part_two('day08_part_two_test.txt') == 6
    assert part_two('day08_data.txt') == 10151663816849
