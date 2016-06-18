# A plus is a square of which side has an odd length greater than 1 and all of it's cells are zeros, except for the middle row and the middle column: they must be filled with ones. For example, in the matrix below there are two pluses, one inside another:

# 00100
# 00100
# 11111
# 00100
# 00100

# Find the number of pluses in a given square matrix.

# The idea is to iterate through each square, and if its a 1, it can potentially be the center of a plus.
# To check if its a square, we set the initial top left and bottom right of the square and check its borders.
# Thus, we start with a 3x3 square, and if it passes the check, we expand the square to a 5x5 square and check the
# new square's border. Each time it passes, we increment the number of pluses.


def count_pluses(matrix):

    count = 0

    if len(matrix) != len(matrix[0]):
        return count

    # function that checks ONLY the border of the square indicated by 2 pairs of
    # [x,y] coordinates
    def check_square(top_left, bottom_right):
        mid_row = (top_left[0] + bottom_right[0]) // 2
        mid_col = (top_left[1] + bottom_right[1]) // 2

        # check top and bottom border
        for j in range(top_left[1], bottom_right[1] + 1):

            # all entries must be 0 except the entry in the middle column
            if j == mid_col:
                if matrix[top_left[0]][j] != 1 or matrix[bottom_right[0]][j] != 1:
                    return False
            else:
                if matrix[top_left[0]][j] != 0 or matrix[bottom_right[0]][j] != 0:
                    return False

        # check left and right border
        # we can exclude the 4 corners because they've been checked above already
        for i in range(top_left[0] + 1, bottom_right[0]):

            # all entries must be 0 except the entry in the middle row
            if i == mid_row:
                if matrix[i][top_left[1]] != 1 or matrix[i][bottom_right[1]] != 1:
                    return False
            else:
                if matrix[i][top_left[1]] != 0 or matrix[i][bottom_right[1]] != 0:
                    return False

        return True

    # we can skip the border of the original matrix because its not possible for the center
    # of a plus to be on the border
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix) - 1):

            # if 1, potentially a center
            if matrix[i][j] == 1:

                # set initial corners
                top_left = [i - 1, j - 1]
                bottom_right = [i + 1, j + 1]

                # while square doesn't exceed the matrix
                while top_left[0] >= 0 and top_left[1] >= 0 and bottom_right[0] < len(matrix) and bottom_right[1] < len(matrix):

                    # if check passes, expand the square
                    if check_square(top_left, bottom_right):
                        count += 1
                        top_left[0] -= 1
                        top_left[1] -= 1
                        bottom_right[0] += 1
                        bottom_right[1] += 1
                    else:
                        break

    return count

mat = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]

mat = [
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0],
    [0,1,0,1,0,0,1,1,1],
    [1,1,1,1,0,0,0,1,0]
]

print(count_pluses(mat))