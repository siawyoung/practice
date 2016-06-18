
# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

# The way to do this is with DP.

# Construct a table of width m where m is the number of coins and n where n is the amount. We assume that the smallest denomination is 1 so the maximum number of coins that can make up the amount is m anyway.

import unittest

def fn(denoms, amt):
    table = [ 0 ] * (amt + 1)
    table[0] = 1
    for i in denoms:
        for j in range(i, amt + 1):
            table[j] += table[j - i]
    return table[amt]


class TestSuite(unittest.TestCase):

    def test_1(self):
        self.assertEqual(fn([2,3], 4), 1)

    def test_2(self):
        self.assertEqual(fn([1,2], 4), 3)


try:
    unittest.main()
except:
    pass
