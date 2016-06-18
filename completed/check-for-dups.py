
# Write a function which finds any integer that appears more than once in a list. The list of length n only contains integers from 1 to n - 1. Optimize for space.

# Since the integers only go from 1 to n - 1, we can abuse that fact. The strategy here is to use the array itself as a marker, but treating the item at the current iteration as an index, and changing the item at THAT index to negative. When we meet a number that is already negative, we will know that it was previously marked, thus returning it as a duplicate.

def check_for_dups(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] > 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return arr[i]

arr = [1,2,5,2,3,1]

print(check_for_dups(arr))

