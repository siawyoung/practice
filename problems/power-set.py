
# Implement a method that takes as input a set S of distinct elements, and prints the power set of S. Print the subsets one per line, with elements separated by commas.

import math

# power_set :: [Int] -> [[Int]]
def power_set(input_set):

    power_set = []

    for i in range(int(math.pow(2, len(input_set)))):
        curr_set = []
        bin_list = list(bin(i).replace('0b', '').zfill(len(input_set)))

        for index, j in enumerate(bin_list):
            if j == '1':
                curr_set.append(input_set[index])

        power_set.append(curr_set)

    return power_set

print(power_set([1,2,3]))
