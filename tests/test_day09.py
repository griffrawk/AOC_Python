from aoc2023.day09.day09 import part_one_two


def test_part_one():
    assert part_one_two('day09_test.txt') == 114
    assert part_one_two('day09_data.txt') == 2043677056


def test_part_two():
    assert part_one_two('day09_test.txt', reverse=True) == 2
    assert part_one_two('day09_data.txt', reverse=True) == 1062
