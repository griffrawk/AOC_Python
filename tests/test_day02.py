from aoc2023.day02.day02 import part_one, part_one_two_combined


def test_part_one():
    assert part_one() == 2105


def test_part_one_two():
    assert part_one_two_combined() == (2105, 72422)
