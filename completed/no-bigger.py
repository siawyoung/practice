

# Given an un unordered array of positive integers, make sure no group of integers of size bigger than M have the same integers.

# the strategy is to iterate from left to right, keeping track of the current size of the group of same integers. Once it exceeds the limit, we start to look for a letter that is different, and whent that happens, we swap it to where the offending position is. At this point, the group will have decreased in size by one. If it's still larger than the limit, we continue to look for different characters to swap back, until the group is within the size limit.

def no_bigger(arr, m):

    curr_length = 0
    exceeded = False
    curr_char = arr[0]

    for i in range(len(arr)):
        if exceeded and curr_char != arr[i]:
            swap_pointer = i
            swap_number = curr_length
            while swap_number > m:
                arr[swap_pointer], arr[swap_pointer - 1] = arr[swap_pointer - 1], arr[swap_pointer]
                swap_number -= 1
                swap_pointer -= 1
            curr_length -= 1
            if curr_length <= m:
                exceeded = False

        elif curr_char == arr[i]:
            curr_length += 1
            if curr_length > m:
                exceeded = True

        curr_char = arr[i]

arr = [3,3,3,1,1,1,2,2,3]
arr = [2,2,2,2,2,2,3,3,3]
no_bigger(arr, 2)
print(arr)
