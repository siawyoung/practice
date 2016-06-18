
import heapq

# Given a list_of_ints, find the highest_product you can get from three of the integers.

def product_of_three(arr):
    min_so_far = float('inf')

    top1 = float('-inf')
    top2 = float('-inf')
    top3 = float('-inf')

    bottom1 = float('inf')
    bottom2 = float('inf')

    for i in arr:
        if i > top1:
            top3 = top2
            top2 = top1
            top1 = i
        elif i > top2:
            top3 = top2
            top2 = i
        elif i > top3:
            top3 = i

        if i < bottom1:
            bottom2 = bottom1
            bottom1 = i
        elif i < bottom2:
            bottom2 = i

    return max(top1 * bottom1 * bottom2, top1 * top2 * top3)

arr = [-14, 10, 21, 1]

print(product_of_three(arr))

