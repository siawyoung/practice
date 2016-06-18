
# Write a program that computes the maximum value of fish a fisherman can catch on a path from the upper leftmost point to the lower rightmost point. The fisherman can only move down or right.

# catch_fish :: [[Int]] -> Int
def catch_fish(matrix):

    table = [ [ 0 for y in range(len(matrix[0]) + 1) ] for x in range(len(matrix) + 1) ]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            table[i + 1][j + 1] = max(table[i][j + 1], table[i + 1][j]) + matrix[i][j]

    print(table)
    return table[-1][-1]


matrix = [
    [0,14,20,1],
    [30,1,0,2],
    [14,16,1,3]
]

print(catch_fish(matrix))