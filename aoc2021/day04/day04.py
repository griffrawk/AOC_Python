import unittest


class TestMethods(unittest.TestCase):

    # def test_part11(self):
    #     ones = {}
    #     zeroes = {}
    #     with open('day03_data.txt', 'r', encoding='utf-8') as a_file:
    #         for a_line in a_file:
    #             a_line = a_line.rstrip()
    #             for (pos, bit) in enumerate(a_line):
    #                 # init dict pos if not in
    #                 if pos not in ones:
    #                     ones[pos] = 0
    #                 if pos not in zeroes:
    #                     zeroes[pos] = 0
    #                 # inc dict count
    #                 if bit == '1':
    #                     ones[pos] += 1
    #                 elif bit == '0':
    #                     zeroes[pos] += 1
    #
    #         gammabits = epsilonbits = ''
    #         for (pos, count) in ones.items():
    #             if count > zeroes[pos]:
    #                 gammabits += '1'
    #                 epsilonbits += '0'
    #             else:
    #                 gammabits += '0'
    #                 epsilonbits += '1'
    #         gamma = int(gammabits, 2)
    #         epsilon = int(epsilonbits, 2)
    #         print('Power consumption = {}'.format(gamma * epsilon))
    #         self.assertEqual(gamma * epsilon, 1997414)
    #
    # def test_part22(self):
    #     with open('day03_data.txt', 'r', encoding='utf-8') as a_file:
    #         bitlist = [[int(bit) for bit in word.strip()] for word in a_file]
    #         oxygen = process(bitlist, 1)
    #         co2 = process(bitlist, 0)
    #         print('Life Support rating = {}'.format(oxygen * co2))
    #         self.assertEqual(oxygen * co2, 1032597)

    def test_part1(self):
        with open('day04_test.txt', 'r', encoding='utf-8') as in_file:
            for inp in in_file:
                inp = inp.strip()
                print(inp)



if __name__ == '__main__':
    unittest.main()
