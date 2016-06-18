
#  Design an efficient algorithm that takes a sorted array A of distinct integers, and returns an index i such that A[i] = i or indicate that no such index exist by returning -1.

# value_matching_index :: [Int] -> Int

def value_matching_index(arr):

    l = 0
    u = len(arr) - 1

    while True:
        if l > u:
            return -1

        m = (u + l) // 2

        if arr[m] > m:
            u = m - 1
        elif arr[m] == m:
            return m
        else:
            l = m + 1

arr = [0,2,6,9,10]

print(value_matching_index(arr))