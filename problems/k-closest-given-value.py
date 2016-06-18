
# Given a sorted array arr[] and a value X, find the k closest elements to X in arr[].

# Ths strategy is to find the "crossing-over" point, if such a point exists. If a point like that exists, we can gather all the k closest elements around that point. If such a point doesn't exist (X is smaller or larger than the smallest or largest element in arr, then we simply return k-th slice of that arr). Overall time is O(logn + k).

import unittest

def k_closest(arr, x, k):

    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]
    assert k <= len(arr) - 1

    l = 0
    u = len(arr) - 1
    while l <= u:
        m = (l + u) // 2

        if m == 0:
            return arr[:k]

        if m == len(arr) - 1:
            return arr[-k:]

        if (arr[m] <= x and arr[m + 1] >= x) or (arr[m - 1] <= x and arr[m] >= x):
            output = []

            if arr[m] <= x and arr[m + 1] >= x:
                lower_index = m
                upper_index = m + 1
            else:
                lower_index = m - 1
                upper_index = m

            while len(output) < k:
                if abs(arr[lower_index] - x) < abs(arr[upper_index] - x):
                    output.append(arr[lower_index])
                    lower_index -= 1
                else:
                    output.append(arr[upper_index])
                    upper_index += 1

            return output
        else:
            if arr[m] > x:
                u = m - 1
            else:
                l = m + 1

class TestSuite(unittest.TestCase):

    arr = [0,1,2,3,4,5,6]

    def test_0(self):
        self.assertEqual(1,1)

    def test_1(self):
        self.assertEqual(k_closest(self.arr, 3, 1), [3])

    def test_2(self):
        self.assertEqual(k_closest(self.arr, -2, 2), [0,1])

    def test_3(self):
        self.assertEqual(k_closest(self.arr, 7, 3), [4,5,6])

try:
    unittest.main()
except:
    pass
