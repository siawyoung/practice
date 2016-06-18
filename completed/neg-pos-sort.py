

# Give you an array which has n integers,it has both positive and negative integers.Now you need sort this array in a special way.After that,the negative integers should in the front,and the positive integers should in the back.Also the relative position should not be changed.
# eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.


# neg_pos_sort :: [Int] -> void

def neg_pos_sort(arr):

    for i in range(len(arr)):
        j = i
        if arr[j] < 0:
            while j > 0 and arr[j - 1] >= 0:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                j -= 1

    return arr

arr = [-1,1,3,-2,2, -2, 1,2]

print(neg_pos_sort(arr))




