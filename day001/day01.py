# day001.py
# --- Day 1: Sonar Sweep ---

def part_one():
    previous = 0
    count = 0
    with open('day01_data.txt', 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            current = int(a_line.rstrip())
            if current > previous != 0:
                count += 1
            previous = current
    print('Depth measurement increases {} times'.format(count))
    assert count == 1665


def part_two():
    previous = 0
    count = 0
    input_count = 0
    d_0 = d_1 = d_2 = 0

    with open('day01_data.txt', 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            input_count += 1
            d_2 = d_1
            d_1 = d_0
            d_0 = int(a_line.rstrip())
            current = d_2 + d_1 + d_0
            if current > previous != 0 and input_count > 3:
                count += 1
            previous = current
    print('Depth measurement increases {} times, in a 3 measurement sliding window'.format(count))


if __name__ == '__main__':
    part_one()
    part_two()

# TODO -- part 2 --
