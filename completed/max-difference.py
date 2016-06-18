
# Google interview question (it's hard! Requires prior knowledge of maximum-subarray problem)

# Given an array of both positive and negative integers, find 2 disjoint contiguous arrays such that the absolute difference between their sums is the greatest.

# the strategy here is to apply the maximum subarray algorithm AND a (modified) minimum subarray from left to right, and do the same from right to left. After this preprocessing step is done, you can then iterate through and for "partition" see which min/max subarray pair on either side yields the largest absolute difference.

# Despite the many passes (4 times for preprocessing, 1 for computing max difference), its still a linear time solution.

def max_difference(arr):

    def find_left_subarrays():
        all_max_indexes = []
        all_min_indexes = []

        curr_max_starting_index = 0
        curr_max_ending_index = 0
        overall_max_starting_index = 0
        overall_max_ending_index = 0
        max_so_far = float('-inf')
        max_ending_here = float('-inf')

        curr_min_starting_index = 0
        curr_min_ending_index = 0
        overall_min_starting_index = 0
        overal_min_ending_index = 0
        min_so_far = float('inf')
        min_ending_here = float('inf')

        for index in range(len(arr)):

            curr = arr[index]

            # if the subarray ending at the current index is less than the item of the current index
            # reset the current subarray ending
            if max_ending_here + curr < curr:

                curr_max_starting_index = index
                curr_max_ending_index = index

            max_ending_here = max(max_ending_here + curr, curr)

            # if the max ending here exceeds the max so far
            # update the overall max indices and the current ending index
            if max_ending_here > max_so_far:
                curr_max_ending_index = index

                overall_max_starting_index = curr_max_starting_index
                overall_max_ending_index = curr_max_ending_index

            max_so_far = max(max_ending_here, max_so_far)

            all_max_indexes.append((overall_max_starting_index, overall_max_ending_index, max_so_far))

            # minimum
            if min_ending_here + curr > curr:
                curr_min_starting_index = index
                curr_min_ending_index = index

            min_ending_here = min(min_ending_here + curr, curr)

            if min_ending_here < min_so_far:
                curr_min_ending_index = index

                overall_min_starting_index = curr_min_starting_index
                overal_min_ending_index = curr_min_ending_index

            min_so_far = min(min_ending_here, min_so_far)

            all_min_indexes.append((overall_min_starting_index, overal_min_ending_index, min_so_far))

        return (all_min_indexes, all_max_indexes)

    def find_right_subarrays():
        all_max_indexes = []
        all_min_indexes = []

        curr_max_starting_index = len(arr) - 1
        curr_max_ending_index = len(arr) - 1
        overall_max_starting_index = len(arr) - 1
        overall_max_ending_index = len(arr) - 1
        max_so_far = float('-inf')
        max_ending_here = float('-inf')

        curr_min_starting_index = len(arr) - 1
        curr_min_ending_index = len(arr) - 1
        overall_min_starting_index = len(arr) - 1
        overal_min_ending_index = len(arr) - 1
        min_so_far = float('inf')
        min_ending_here = float('inf')

        for index in range(len(arr) - 1, -1, -1):

            curr = arr[index]

            if max_ending_here + curr < curr:

                curr_max_starting_index = index
                curr_max_ending_index = index

            max_ending_here = max(max_ending_here + curr, curr)

            if max_ending_here > max_so_far:
                curr_max_ending_index = index

                overall_max_starting_index = curr_max_starting_index
                overall_max_ending_index = curr_max_ending_index

            max_so_far = max(max_ending_here, max_so_far)

            all_max_indexes = [(overall_max_ending_index, overall_max_starting_index, max_so_far)] + all_max_indexes

            if min_ending_here + curr > curr:
                curr_min_starting_index = index
                curr_min_ending_index = index

            min_ending_here = min(min_ending_here + curr, curr)

            if min_ending_here < min_so_far:
                curr_min_ending_index = index

                overall_min_starting_index = curr_min_starting_index
                overal_min_ending_index = curr_min_ending_index

            min_so_far = min(min_ending_here, min_so_far)

            all_min_indexes = [(overal_min_ending_index, overall_min_starting_index, min_so_far)] + all_min_indexes

        return (all_min_indexes, all_max_indexes)

    all_min_prefix_arrays, all_max_prefix_arrays = find_left_subarrays()
    all_min_suffix_arrays, all_max_suffix_arrays = find_right_subarrays()

    largest_difference_so_far = 0
    left_array_range = None
    right_array_range = None

    for i in range(1, len(arr)):
        left_min_right_max_diff = abs(all_min_prefix_arrays[i-1][2] - all_max_prefix_arrays[i][2])

        if left_min_right_max_diff > largest_difference_so_far:
            left_array_range = all_min_prefix_arrays[i-1][0:2]
            right_array_range = all_max_prefix_arrays[i][0:2]
            largest_difference_so_far = left_min_right_max_diff

        left_max_right_min_diff = abs(all_max_prefix_arrays[i-1][2] - all_min_suffix_arrays[i][2])

        if left_min_right_max_diff > largest_difference_so_far:
            left_array_range = all_max_prefix_arrays[i-1][0:2]
            right_array_range = all_min_suffix_arrays[i][0:2]
            largest_difference_so_far = left_min_right_max_diff


    return (left_array_range, right_array_range)

# arr = [-1,4,2,5,1,2,5,-1,2,3]

arr = [1,2,-5, 3,4]

print(max_difference(arr))

