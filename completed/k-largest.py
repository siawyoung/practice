
#  Design an algorithm for computing the k-th largest element in an array A that runs in O(n) expected time.

## We use an idea from quick sort

## Pick a number at random (we choose the leftmost), then partition it ala quick sort. If the index of the chosen number matches the k-th largest number, then we terminate. Else if the index is larger then the k-th largest number, we partition on the left subarray, else we partition on the right subarray.

# kth_largest :: [Int] -> Int -> Maybe(Int)
def kth_largest(arr, k):

    if k > len(a):
        return None

    l = 0
    u = len(arr) - 1

    while True:
        pivot_value = arr[l] # just pick the left-most as pivot
        m = l

        for i in range(l+1, u+1):
            if arr[i] < pivot_value:
                m += 1
                arr[i], arr[m] = arr[m], arr[i]
        arr[m], arr[l] = arr[l], arr[m]

        if m == len(arr) - k:
            return arr[m]

        elif m > len(arr) - k:
            u = m - 1

        else:
            l = m + 1

# expected: kth_largest([], 1) -> None
# expected: kth_largest([1,3,2,4], 2) -> 3
# expected: kth_largest([1], 2) -> None

a = [0,1,2]

print(kth_largest(a, 3))