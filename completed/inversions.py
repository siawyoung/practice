
# Design an efficient algorithm that takes an array A of n numbers and returns the number of inverted pairs of indices.

# The number of inversions is the number of times insertion sort runs.

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

# count_inversions :: [Int] -> Int
def count_inversions(arr):

    if not arr:
        return 0

    count = 0

    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            swap(arr, j, j-1)
            count += 1
            j -= 1

    return count

arr = [4,3,2,1]
print(count_inversions(arr))