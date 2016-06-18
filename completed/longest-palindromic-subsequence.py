# Find the longest palindromic subsequence.

# 2D DP
# fill it diagonally from the top left to bottom right, ending at the top right corner.

import unittest

def lps(string):

    table = [ [0] * len(string) for _ in range(len(string)) ]

    for i in range(len(string)):
        table[i][i] = 1

    for substring_length in range(2, len(string) + 1):
        for i in range(len(string) - substring_length + 1):
            j = i + substring_length - 1

            if string[i] == string[j] and substring_length == 2:
                table[i][j] = 2

            elif string[i] == string[j]:
                table[i][j] = table[i + 1][j - 1] + 2

            else:
                table[i][j] = max(table[i + 1][j], table[i][j - 1])

    return table[0][len(string) - 1]

class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lps('BBABCBCAB'), len('BABCBAB'))

try:
    unittest.main()
except:
    pass