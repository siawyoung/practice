
# Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths (in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

# iterate through once, and add the other "half" into a hash map. If future ones match anything in the hash map, we have a match!

# e.g. [1,6,2,3], sum = 7
# i = 1, add 7-1 = 6 into set

def find_sum(_sum, arr):
    other_pair_set = set()
    for i in arr:
        if i not in other_pair_set:
            other_pair_set.add(_sum - i)
        else:
            return True
    return False

_sum = 12
arr = [1,6,2,3,4,8]

print(find_sum(_sum, arr))
