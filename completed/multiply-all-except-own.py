
# input [2,3,1,4]
# output [12,8,24,6]

# Multiply all fields except it's own position.

# Restrictions:
# 1. no use of division
# 2. complexity in O(n)

def multiply_all_except_own(arr):

    left_prefix_product = [1] * len(arr)
    right_prefix_product = [1] * len(arr)

    left_product = 1
    right_product = 1

    for i in range(1, len(arr)):
        left_product *= arr[i - 1]
        left_prefix_product[i] = left_product

    for i in range(len(arr) - 2, -1, -1):
        right_product *= arr[i + 1]
        right_prefix_product[i] = right_product

    return [ a * b for a, b in zip(left_prefix_product, right_prefix_product) ]

arr = [2,3,1,4]
print(multiply_all_except_own(arr))
