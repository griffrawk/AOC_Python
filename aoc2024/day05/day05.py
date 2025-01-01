import os


def part_one_two(file):
    res = 0
    corres = 0
    rules = set()
    updates = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            if '|' in a_line:
                rules.add(a_line.strip())
            if ',' in a_line:
                updates.append(a_line.strip().split(','))

    class ContinueU(Exception):
        pass

    for update in updates:
        corrected = False
        try:
            for idx in range(0, len(update)):
                for fwdref in range(idx + 1, len(update)):
                    key = f'{update[idx]}|{update[fwdref]}'
                    if not key in rules:
                        key = f'{update[fwdref]}|{update[idx]}'
                        if key in rules:
                            corrected = True
                            # swap
                            temp = update[fwdref]
                            update[fwdref] = update[idx]
                            update[idx] = temp
                        else:
                            # Python in its infinite wisdom still doesn't have labelled
                            # continue or break, so you have to raise an exception
                            raise ContinueU
        except ContinueU:
            continue

        middle = int(abs(len(update) / 2))
        if corrected:
            corres += int(update[middle])
        else:
            res += int(update[middle])

    return res, corres


def part_one_two_alt(file):
    res = 0
    corres = 0
    rules = set()
    updates = []
    with open(os.path.join(os.path.dirname(__file__), file), 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            if '|' in a_line:
                rules.add(a_line.strip())
            if ',' in a_line:
                updates.append(a_line.strip().split(','))

    for update in updates:
        corrected = False
        for idx in range(0, len(update)):
            for fwdref in range(idx + 1, len(update)):
                key = f'{update[idx]}|{update[fwdref]}'
                if not key in rules:
                    key = f'{update[fwdref]}|{update[idx]}'
                    if key in rules:
                        corrected = True
                        # swap
                        temp = update[fwdref]
                        update[fwdref] = update[idx]
                        update[idx] = temp
                    else:
                                # this is even messier than the exception example!
                        break   # out of fwdref as neither combo found
            else:
                continue        # fwdref completed, so continue idx loop
            continue            # fwdref break, so continue update loop rather than pick middle
                                # for this update
                                # having only indentation doesn't help the comprehension either!
        # idx completed, so pick middle
        middle = int(abs(len(update) / 2))
        if corrected:
            corres += int(update[middle])
        else:
            res += int(update[middle])

    return res, corres


def test_part_one_two_test():
    assert part_one_two_alt('day05_test.txt') == (143, 123)


def test_part_one_two_data():
    assert part_one_two_alt('day05_data.txt') == (4569, 6456)
