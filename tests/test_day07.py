from aoc2023.day07.day07 import part_one_two, analyse_hand


def test_part_one_two():
    # day07_test.txt
    assert part_one_two('day07_test.txt', play_joker=False) == 6440
    assert part_one_two('day07_test.txt', play_joker=True) == 5905

    # day07_data.txt
    assert part_one_two('day07_data.txt', play_joker=False) == 252656917
    assert part_one_two('day07_data.txt', play_joker=True) == 253499763


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

    assert analyse_hand('AJAAK', True) == 'four'
    assert analyse_hand('JJJJJ', True) == 'five'
    assert analyse_hand('23456', True) == 'high'
    assert analyse_hand('KTJJT', True) == 'four'
    assert analyse_hand('12JJ4', True) == 'three'
    assert analyse_hand('11JJ4', True) == 'four'
