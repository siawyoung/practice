
# Find the number of perfect squares in [A,B], both ends inclusive.

import math

def perfect_squares(A, B):
    if B < 0:
        return 0

    starting_number = int(math.floor(math.sqrt(A))) if A >= 0 else 0
    ending_number = int(math.floor(math.sqrt(B))) + 1

    count = 0

    for i in range(starting_number, ending_number):
        if math.pow(i,2) >= A and math.pow(i,2) <= B:
            count += 1

    return count
