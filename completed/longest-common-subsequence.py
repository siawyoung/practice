
# Given 2 arrays, find the longest subsequence problem.

# Dynamic programming, similar to 0-1 knapsack or edit distance problems

import unittest

def longest_common_subsequence(arr1, arr2):

    table = [ [None] * (len(arr2) + 1) for _ in range(len(arr1) + 1) ]

    for i in range(len(arr1) + 1):
        for j in range(len(arr2) + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif arr1[i - 1] == arr2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])


    index = table[len(arr1)][len(arr2)]


    lcs = [ None ] * index

    i = len(arr1)
    j = len(arr2)

    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            lcs[index - 1] = arr1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif table[i - 1][j] > table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs



class TestSuite(unittest.TestCase):

    arr1 = [0,1,2]
    arr2 = [2]
    arr3 = [1,5,7,2]

    def test_1(self):
        self.assertEqual(longest_common_subsequence(self.arr1, self.arr2), [2])

    def test_2(self):
        self.assertEqual(longest_common_subsequence(self.arr1, self.arr3), [1,2])

try:
    unittest.main()
except:
    pass