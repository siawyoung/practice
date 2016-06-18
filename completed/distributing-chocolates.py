# Christy is interning at HackerRank. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and may have distributed the chocolates unequally. One of the program managers gets to know this and orders Christy to make sure everyone gets equal number of chocolates.

# But to make things difficult for the intern, she is ordered to equalize the number of chocolates for every colleague in the following manner,

# For every operation, she can choose one of her colleagues and can do one of the three things.

# She can give one chocolate to every colleague other than chosen one.
# She can give two chocolates to every colleague other than chosen one.
# She can give five chocolates to every colleague other than chosen one.
# Calculate minimum number of such operations needed to ensure that every colleague has the same number of chocolates.

# The idea is that giving X chocolates to everyone except 1 person is equivalent to taking away X chocolates from that person. Therefore, we can find the answer by finding how many times we need to take 1,2, or 5 chocolates from anybody until everyone has the same number of chocolates.

import unittest

def distribute_chocolate(arr):

    _min = min(arr)
    count = 0
    for i in arr:
        temp = i
        while temp > _min:
            if temp - 5 >= _min:
                temp -= 5
            elif temp - 2 >= _min:
                temp -= 2
            else:
                temp -= 1
            count += 1

    return count


class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(distribute_chocolate([2,2,3,7]), 2)

try:
    unittest.main()
except:
    pass
