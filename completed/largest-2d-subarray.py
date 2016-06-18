
from largest_rectangle import largest_rectangle

def largest_2d_subarray(matrix):

    max_height_table = [ [0] * len(matrix[0]) for i in range(len(matrix)) ]

    for i in range(len(matrix) - 1, -1, -1):
        row = matrix[i]

        # special case for last row
        if i == len(matrix) - 1:
            max_height_table[len(matrix) - 1] = row
            continue

        for j, column in enumerate(row):
            if column == 0:
                continue
            max_height_table[i][j] = max_height_table[i + 1][j] + 1


    max_area = 0

    for i in range(len(matrix)):
        largest_subarray_area = largest_rectangle(max_height_table[i])
        max_area = max(max_area, largest_subarray_area)

    return max_area



matrix = [
    [1,1,0,1,0],
    [1,1,1,1,0],
    [0,1,1,1,1],
    [0,1,1,1,1]
]

_max = [
    [2, 4, 0, 1, 0],
    [1, 3, 3, 0, 0],
    [0, 2, 2, 2, 2],
    [0, 1, 1, 1, 1]
]

print(largest_2d_subarray(matrix))