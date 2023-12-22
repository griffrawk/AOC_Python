import os
import itertools


# Provide a sort key for a card hand based on card letters representing values
# for the ten, court cards and aces high.
def hand_sort_key(hand_bid):
    hand = hand_bid[0]
    court = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
    key = ''
    for c in hand:
        if c.isdigit():
            key += '0' + c
        else:
            key += (court.get(c, ''))
    return key


# Return a hand rank based on cards in the hand
def analyse_hand(hand):
    three = False
    pair = high = 0
    hand_rank = ''
    for _, type_group in itertools.groupby(sorted(hand)):
        match len(list(type_group)):
            case 5:
                hand_rank = 'five'
            case 4:
                hand_rank = 'four'
            case 3:
                three = True
                hand_rank = 'three'
            case 2:
                pair += 1
                hand_rank = 'pair'
            case 1:
                high += 1
    if three and pair == 1:
        hand_rank = 'fullhouse'
    if pair > 1:
        hand_rank = 'twopair'
    if high == 5:
        hand_rank = 'high'
    return hand_rank


def part_one():
    game = {'high': [], 'pair': [], 'twopair': [], 'three': [], 'fullhouse': [], 'four': [], 'five': []}
    with open(os.path.join(os.path.dirname(__file__), "day07_data.txt"), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            # print(a_line)
            hand, bid = a_line.split()
            hand_rank = analyse_hand(hand)
            s = game.get(hand_rank, [])
            s.append((hand, bid))
            game[hand_rank] = s

    # Play back the hands in rank order, sorted within rank by cards
    winnings = 0
    game_rank = 1
    for hands in game.values():
        for hand, bid in sorted(hands, key=hand_sort_key):
            winnings += int(bid) * game_rank
            game_rank += 1

    print(winnings)
    return winnings


def test_part_one():
    # assert part_one() == 6440
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
