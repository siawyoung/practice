
# You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

# Consider the following 6 activities.
#      start[]  =  {1, 3, 0, 5, 8, 5};
#      finish[] =  {2, 4, 6, 7, 9, 9};
# The maximum set of activities that can be executed
# by a single person is {0, 1, 3, 4}

# This problem can be solve greedily, by taking the activities by finish time and greedily picking the closest activity whose finish time is the smallest.

import unittest

def max_activities(arr):

    assert arr
    assert len(arr) > 0

    sorted(arr, key=lambda x:x[1])
    output = [0]
    for i in range(len(arr)):
        if arr[i][0] >= arr[output[-1]][1]:
            output.append(i)

    return output

class TestSuite(unittest.TestCase):

    arr1 = [(1,2), (3,4), (0,6), (5,7), (8,9), (5,9)]

    def test_1(self):
        self.assertEqual(max_activities(self.arr1), [0,1,3,4])

try:
    unittest.main()
except:
    pass
