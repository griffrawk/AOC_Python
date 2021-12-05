def part1():
    ones = {}
    zeroes = {}
    gamma = epsilon = 0
    with open('day03_data.txt', 'r', encoding='utf-8') as a_file:
        for a_line in a_file:
            a_line = a_line.rstrip()
            for (pos, bit) in enumerate(a_line):
                # count ones and zeroes in each position from LSB to MSB
                # init dict pos if not in
                if pos not in ones:
                    ones[pos] = 0
                if pos not in zeroes:
                    zeroes[pos] = 0
                # inc dict count
                if bit == '1':
                    ones[pos] += 1
                elif bit == '0':
                    zeroes[pos] += 1

        # gamma = sum of powers of two where '1' is dominant
        # epsilon = sum of powers of two where '0' is dominant
        for (pos, count) in ones.items():
            # 'invert' the pos into a power of 2
            # done this way to set a precedent for part 2 so I dont reverse the string straight after
            # reading it, so simplifying the part2 process
            power = len(ones) - pos - 1
            if count > zeroes[pos]:
                gamma += 2 ** power
            else:
                epsilon += 2 ** power
        print('Power consumption = {}'.format(gamma * epsilon))
        assert gamma * epsilon == 1997414


if __name__ == '__main__':
    part1()
