import copy
import unittest


class TestMethods(unittest.TestCase):

    def test_part1(self):
        ones = {}
        zeroes = {}
        with open('day03_data.txt', 'r', encoding='utf-8') as a_file:
            for a_line in a_file:
                a_line = a_line.rstrip()
                for (pos, bit) in enumerate(a_line):
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

            gammabits = epsilonbits = ''
            for (pos, count) in ones.items():
                if count > zeroes[pos]:
                    gammabits += '1'
                    epsilonbits += '0'
                else:
                    gammabits += '0'
                    epsilonbits += '1'
            gamma = int(gammabits, 2)
            epsilon = int(epsilonbits, 2)
            print('Power consumption = {}'.format(gamma * epsilon))
            self.assertEqual(gamma * epsilon, 1997414)

    def test_part2(self):
        with open('day03_data.txt', 'r', encoding='utf-8') as a_file:
            oxlist = [[int(bit) for bit in word.strip()] for word in a_file]
            co2list = copy.deepcopy(oxlist)
            bitlen = len(oxlist[0])
            for i in range(0, bitlen):
                vertical = [word[i] for word in oxlist]
                dominant_bit = 1
                if vertical.count(1) < vertical.count(0):
                    dominant_bit = 0
                # rewrite oxlist here before next iteration
                oxlist = [word for word in oxlist if word[i] == dominant_bit]
                if len(oxlist) == 1:
                    break
            oxygen = int(''.join([str(i) for i in oxlist[0]]), 2)
            for i in range(0, bitlen):
                vertical = [word[i] for word in co2list]
                dominant_bit = 0
                if vertical.count(1) < vertical.count(0):
                    dominant_bit = 1
                # rewrite co2list here before next iteration
                co2list = [word for word in co2list if word[i] == dominant_bit]
                if len(co2list) == 1:
                    break
            co2 = int(''.join([str(i) for i in co2list[0]]), 2)

            print('Life Support rating = {}'.format(oxygen * co2))
            self.assertEqual(oxygen * co2, 1032597)


if __name__ == '__main__':
    unittest.main()
