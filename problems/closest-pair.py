
# Find the closest pair in 2 sorted arrays.

# Start with two pointers at the start of each array, and compare the absolute difference between them, updating the closest pair if necessary, and moving the smaller pointer rightward at each iteration. If we reach a point where 2 pointers have the same value, we can return them prematurely, since they are as close as it will get.

import unittest

def closest_pair(arr1, arr2):
    arr1_pointer = 0
    arr2_pointer = 0

    diff = float('inf')

    closest_pair = None

    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):

        if abs(arr1[arr1_pointer] - arr2[arr2_pointer]) < diff:
            diff = abs(arr1[arr1_pointer] - arr2[arr2_pointer])
            closest_pair = (arr1[arr1_pointer], arr2[arr2_pointer])

        if arr1[arr1_pointer] < arr2[arr2_pointer]:
            arr1_pointer += 1
        elif arr1[arr1_pointer] > arr2[arr2_pointer]:
            arr2_pointer += 1
        else:
            return closest_pair

    return closest_pair


class TestSuite(unittest.TestCase):

    arr1 = [0,2,5,12]
    arr2 = [3,7,15]

    def test_1(self):
        self.assertEqual(closest_pair(self.arr1, self.arr2), (2,3))

try:
    unittest.main()
except:
    pass

