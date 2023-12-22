from aoc2023.day07.day07 import part_one, analyse_hand


def test_part_one():
    # day07_test.txt
    # assert part_one() == 6440

    # day07_data.txt
    assert part_one() == 252656917


def test_analyse_hand():
    assert analyse_hand('32T3K') == 'pair'
    assert analyse_hand('T55J5') == 'three'
    assert analyse_hand('KK677') == 'twopair'
    assert analyse_hand('KTJJT') == 'twopair'
    assert analyse_hand('QQQJA') == 'three'
    assert analyse_hand('Q23JA') == 'high'
    assert analyse_hand('3233A') == 'three'
    assert analyse_hand('8233A') == 'pair'
    assert analyse_hand('AAAAA') == 'five'
    assert analyse_hand('AKAAK') == 'fullhouse'
    