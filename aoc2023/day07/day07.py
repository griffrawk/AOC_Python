import os
import itertools
import re


# Return a hand rank based on cards in the hand
def analyse_hand(hand, play_joker=False):
    three = False
    pair = high = 0
    hand_rank = ''
    jokers = 0
    for _, type_group in itertools.groupby(sorted(hand)):
        gtype = list(type_group)
        # if play_joker and J present, count them instead of assigning a rank. The other cards in
        # the hand decide the rank, which is then modified by jokers, if any
        if 'J' in gtype and play_joker:
            jokers = len(gtype)
            continue
        match len(gtype):
            case 5:
                hand_rank = 'five'
            case 4:
                hand_rank = 'four'
            case 3:
                hand_rank = 'three'
            case 2:
                pair += 1
                hand_rank = 'pair'
            case 1:
                high += 1
    # Summarise for hand if necessary
    if hand_rank == 'three' and pair == 1:
        hand_rank = 'fullhouse'
    if pair > 1:
        hand_rank = 'twopair'
    if high + jokers == 5:
        hand_rank = 'high'

    # Adjust rank based on number of Jokers found
    match jokers:
        case 5:
            hand_rank = 'five'
        case 4:
            hand_rank = 'five'
        case 3:
            match hand_rank:
                case 'pair':
                    hand_rank = 'five'
                case 'high':
                    hand_rank = 'four'
        case 2:
            match hand_rank:
                case 'three':
                    hand_rank = 'five'
                case 'pair':
                    hand_rank = 'four'
                case 'high':
                    hand_rank = 'three'
        case 1:
            match hand_rank:
                case 'four':
                    hand_rank = 'five'
                case 'twopair':
                    hand_rank = 'fullhouse'
                case 'three':
                    hand_rank = 'four'
                case 'pair':
                    hand_rank = 'three'
                case 'high':
                    hand_rank = 'pair'
    return hand_rank


def part_one_two(file, play_joker):
    game = {'high': [], 'pair': [], 'twopair': [], 'three': [], 'fullhouse': [], 'four': [], 'five': []}

    # Analyse each hand and push each hand, and it's bid into a list for rank
    with open(os.path.join(os.path.dirname(__file__), file), "r", encoding="utf-8") as a_file:
        for a_line in a_file:
            a_line = a_line.strip()
            # print(a_line)
            hand, bid = a_line.split()
            hand_rank = analyse_hand(hand, play_joker)
            s = game.get(hand_rank, [])
            s.append((hand, bid))
            game[hand_rank] = s

    # Play back the hands in rank order, sorted within rank by cards
    # (e.g. pairs: 'KK7QA' > 'KK2QA' > 'TKTQA')
    winnings = 0
    inc = 1

    # Provide a sort key for a card hand based on card letters representing values
    # for the ten, court cards and aces high.
    def hand_sort_key(hand_bid):
        nonlocal play_joker
        hand = hand_bid[0]
        if play_joker:
            court = {'J': '01', 'T': '10', 'Q': '12', 'K': '13', 'A': '14'}
        else:
            court = {'T': '10', 'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
        key = ''
        for c in hand:
            if c.isdigit():
                key += '0' + c
            else:
                key += (court.get(c, ''))
        return key

    for rank, hand_rank in game.items():
        for hand, bid in sorted(hand_rank, key=hand_sort_key):
            print(re.sub('J', '\u001b[31mJ\u001b[0m', hand), rank, inc)
            winnings += int(bid) * inc
            inc += 1

    print(winnings)
    return winnings
