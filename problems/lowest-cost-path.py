
# Given a cost matrix, find the lowest cost path from (0,0) to a given point in the matrix. The cost of the path includes both the starting and end points. You can traverse down, right, and diagonally right-down.

# Same idea, straightforward DP, watch out for off-by-one errors

import unittest

def lowest_cost_path(matrix, end_point):

    table = [ [float('inf')] * (end_point[1] + 2) for _ in range(end_point[0] + 2)  ]

    table[1][1] = matrix[0][0]

    for i in range(1, end_point[0] + 2):
        for j in range(1, end_point[1] + 2):
            if i == 1 and j == 1:
                continue

            table[i][j] = min(table[i - 1][j], table[i - 1][j - 1], table[i][j - 1]) + matrix[i - 1][j - 1]

    return table[end_point[0] + 1][end_point[1] + 1]


class TestSuite(unittest.TestCase):

    matrix = [
        [1,2,3],
        [4,8,2],
        [1,5,3]
    ]

    p1 = [1,2]

    p2 = [2,1]

    p3 = [1,1]

    def test_1(self):
        self.assertEqual(lowest_cost_path(self.matrix, self.p1), 5)

    def test_2(self):
        self.assertEqual(lowest_cost_path(self.matrix, self.p2), 10)

    def test_3(self):
        self.assertEqual(lowest_cost_path(self.matrix, self.p3), 9)

try:
    unittest.main()
except:
    pass
