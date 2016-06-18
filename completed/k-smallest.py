
# Find the k smallest numbers in an array.

# k_smallest :: [Int] -> [Int]

import random

def partition(arr):
    if len(arr) == 1:
        return ([], arr[0], [])

    if len(arr) == 2:
        if arr[0] <=  arr[1]:
            return ([], arr[0], arr[1])
        else:
            return ([], arr[1], arr[0])

    pivot_index = random.randint(0, len(arr) - 1)

    pivot = arr[pivot_index]

    left = []
    right=  []

    for i in range(len(arr)):
        if i != pivot_index:
            if arr[i] > pivot:
                right.append(arr[i])
            else:
                left.append(arr[i])

    return (left, pivot, right)

def quickselect(arr, k):

    left, pivot, right = partition(arr)
    if len(left) == k - 1:
        return pivot
    elif len(left) > k - 1:
        return quickselect(left, k)
    else:
        return quickselect(right, k - len(left) - 1)


def k_smallest(arr, k):
    kth_smallest = quickselect(arr, k)
    output = []
    count = 0
    for i in range(len(arr)):
        if arr[i] < kth_smallest:
            output.append(arr[i])
            count += 1
    for i in range(len(arr)):
        if arr[i] == kth_smallest and count < k:
            output.append(arr[i])
            count += 1
    return output


arr = [1,6,7,9,3,2,4,1,2]
print(k_smallest(arr, 5))