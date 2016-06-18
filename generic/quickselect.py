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