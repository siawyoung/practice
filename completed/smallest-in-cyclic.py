
# Design an O(logn) algorithm for finding the position of the smallest element in a cyclically sorted array. Assume all elements are distinct.

# insight:
# the smallest element has a larger element behind it, unless its the first element

# start_cyclic :: [Int] -> Int
def start_cyclic(arr):

    l = 0
    u = len(arr) - 1

    def _check(arr, l, u):

        if l > u:
            return None

        m = (l + u) // 2

        if arr[m-1] > arr[m]:
            return m

        return _check(arr, l, m - 1) or _check(arr, m + 1, u)

    return _check(arr, l, u) or 0

# arr = [2,3,4,5,1]
# arr = [1,2,3,4,5]
# arr = [5,1,2,3,4]
arr = [1,2,0]
print(start_cyclic(arr))