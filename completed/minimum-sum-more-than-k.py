
# Given a list of n objects, write a function that outputs the minimum set of numbers that sum to at least K.

# minimum_sum_more_than_k :: [Int] -> Int -> [Int]
def minimum_sum_more_than_k(arr, _sum):

    _set = []
    remainder = _sum

    while True:
        m = -1
        _max = 0
        _max_index = 0

        for i in range(len(arr)):
            if arr[i] > _max:
                _max_index = i
                _max = max(_max, arr[i])
            if arr[i] < remainder:
                m += 1
                arr[m], arr[i] = arr[i], arr[m]


        # if not the last element, the next element is definitely larger than remainder:
        if m < len(arr) - 1:
            _set.append(arr[m + 1])
            return _set

        # if m is last element, we minus the max element and pop it off the arr
        else:
            arr[m], arr[_max_index] = arr[_max_index], arr[m]
            arr.pop()
            _set.append(_max)
            remainder -= _max

    return _set

arr = [3,1,2,4,1,6,2,1,5,7,1]
_sum = 20

print(minimum_sum_more_than_k(arr, _sum))