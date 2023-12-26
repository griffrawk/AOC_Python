from aoc2023.day08.day08 import part_one_two


def test_part_one_two():
    # day07_test.txt
    assert part_one_two('day08_test_1.txt') == 2
    assert part_one_two('day08_test_2.txt') == 6

    # day07_data.txt
    assert part_one_two('day08_data.txt') == 11911


