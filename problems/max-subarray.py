def max_subarray(arr):
    print(arr)
    all_indexes = []
    starting_index = 0
    ending_index = 0
    max_starting_index = 0
    max_ending_index = 0
    max_so_far = float('-inf')
    max_ending_here = float('-inf')
    for index, i in enumerate(arr):

        if max_ending_here + i < i:

            starting_index = index
            ending_index = index

        max_ending_here = max(max_ending_here + i, i)

        if max_ending_here > max_so_far:
            ending_index = index

            max_starting_index = starting_index
            max_ending_index = ending_index

        max_so_far = max(max_ending_here, max_so_far)

        all_indexes.append((max_starting_index, max_ending_index))

arr = [1,-4,1,2,-1,4,1,-5,-10,1,5,-2,3,-1,4,-1,-5]
# arr = [1,-4,1]
# arr = [-1,-2,-3]
print(max_subarray(arr))