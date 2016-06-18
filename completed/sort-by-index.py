
# Write a function that takes an array A and an index i into A, and rearranges the elements such that all elements less than A[i] appear first, followed by elements equal to A[i], followed by elements greater than A[i]. Your algorithm should have 0(1) space complexity and O(|A|)time complexity.

def sort(arr, idx):

  if idx < 0 or idx >= len(arr):
    return

  pivot_value = arr[idx]

  smaller_index = 0
  equal_index   = 0
  larger_index  = len(arr) - 1

  while equal_index <= larger_index:
    if arr[equal_index] < pivot_value:
      arr[equal_index], arr[smaller_index] = arr[smaller_index], arr[equal_index]
      smaller_index += 1
      equal_index += 1

    elif arr[equal_index] == pivot_value:
      equal_index += 1

    else:
      arr[equal_index], arr[larger_index] = arr[larger_index], arr[equal_index]
      larger_index -= 1

arr = [1,2,3,3,3,3,1,2,5,8,4,2,7,2,1]

sort(arr, 1)

print(arr)
