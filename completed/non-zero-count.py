# /*
# Write an algorithm that brings all nonzero elements to the left of the array, and returns the number of nonzero elements.

# Example input: [ 1, 0, 2, 0, 0, 3, 4 ]
# Example output: 4

# [1, 4, 2, 3, 0, 0, 0]

# * The algorithm should operate in place, i.e. shouldn't create a new array.
# * The order of nonzero elements does not matter
# */

def nonzero(arr):
    m = -1

    def swap(a,b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp

    for i in range(len(arr)):
        if arr[i] != 0:
            m += 1
            swap(m, i)

    return m + 1


arr = [0,0,0,1]
print(nonzero(arr))
print(arr)