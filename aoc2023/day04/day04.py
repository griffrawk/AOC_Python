# day02.py
import os


def part_one_two():
    results = {}
    sum_up = 0
    with open(os.path.join(os.path.dirname(__file__), 'day04_data.txt'), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            card, numbers = a_line.split(':')
            card_number = int(card.split()[1])
            left, right = numbers.split('|')
            winning = set([x for x in left.split()])
            draw = set([x for x in right.split()])
            wins = len(winning.intersection(draw))
            if (power := wins - 1) >= 0:
                sum_up += 2 ** power
            results[card_number] = wins

    # part two
    # now a recursive pass through results to total the number of scratchcards
    scratchcards = 0

    def rec(rec_card, rec_draw):
        # 1 for the calling card
        sc = 1
        if rec_draw > 0:
            # draw new cards, and for each, draw new cards...
            for new_card in range(rec_card + 1, rec_card + rec_draw + 1):
                sc += rec(new_card, results[new_card])
        return sc

    for card in results:
        scratchcards += rec(card, results[card])

    print(sum_up, scratchcards)
    return sum_up, scratchcards





