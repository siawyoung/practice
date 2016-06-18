
# If a canoe can hold 2 kids and a max weight of 150 lbs, write a function that returns the minimum number of canoes needed, given a list of kids and their weights.

# Don't need dynamic programming for this - a greedy one will do, since a canoe can only hold 2 kids anyway.

# Sort the list of weights first. Start with one pointer at each end of the sorted list, then move your way to the center, trying to fit 2 kids into a boat at any point in time.

# Overall time is O(nlogn) for the sorting, the putting kids into the boat part is linear.

import unittest

def minimum_boats(arr):

    arr.sort()

    assert arr[-1] <= 150

    lightest_kid = 0
    heaviest_kid = len(arr) - 1
    boats = 0

    while lightest_kid <= heaviest_kid:

        if lightest_kid == heaviest_kid:
            boats += 1
            break

        if arr[lightest_kid] + arr[heaviest_kid - 1] <= 150:
            lightest_kid += 1
            heaviest_kid -= 1
        else:
            heaviest_kid -= 1

        boats += 1

    return boats

class TestSuite(unittest.TestCase):
    def test_1(self):
        self.assertEqual(minimum_boats([54,61,9,15,32,94,23,24,11,23,142]), 7)

unittest.main()
