
import math

# Given a number N, write a program that returns all possible combinations of numbers that add up to N, as lists. (Exclude the N+0=N)

# For example, if N=4 return {{1,1,1,1},{1,1,2},{2,2},{1,3}}

# possible_combinations :: Int -> [[Int]]
def possible_combinations(n):

    def _generate(n):

        if n == 1:
            return [[1]]

        if n == 2:
            return [[1,1]]

        output = []

        for i in range(n - 1, math.ceil(n / 2) - 1, -1):
            output.append([i,n - i])

        smaller_ones = _generate(n-1)

        print(smaller_ones)

        output += [ x + [1] for x in smaller_ones ]

        return output

    return _generate(n)


print(possible_combinations(5))

