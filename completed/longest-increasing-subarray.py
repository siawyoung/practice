
# Design and implement an algorithm that takes as input an array A of n elements, and returns the beginning and ending indices of a longest increasing subarray of A.

# longest_increasing_subarray :: [Int] -> (Int, Int)

def longest_increasing_subarray(arr):

    if not arr:
        return (-1,-1)

    if len(arr) == 1:
        return (0,0)

    max_length = 1
    curr_length = 1

    curr_max_start = 0
    curr_max_end = 0

    curr_start = 0
    curr_end = 0

    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            curr_end += 1
            curr_length += 1

        else:
            if curr_length > max_length:
                max_length = curr_length
                curr_max_start = curr_start
                curr_max_end = curr_end

            curr_start = i
            curr_end = i

    if curr_length > max_length:
        curr_max_start = curr_start
        curr_max_end = curr_end

    return (curr_max_start, curr_max_end)

# longest_increasing_subarray([3,1,2,5]) -> (1,3)
# longest_increasing_subarray([0]) -> (0,0)
# longest_increasing_subarray([]) -> (-1,-1)
# longest_increasing_subarray([1,0]) -> (0,0) or (1,1)

print(longest_increasing_subarray([3,1,2,5]))
print(longest_increasing_subarray([2,3,1]))
print(longest_increasing_subarray([1,0]))