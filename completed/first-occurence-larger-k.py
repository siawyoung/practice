 # Design an efficient algorithm that takes a sorted array A and a key k, and finds the index of the first occurrence an element larger than k; return -1 if every element is less than or equal to k. For example, when applied to the array in Figure 11.1 your algorithm should return -1 if k = 500; if k = 101, your algorithm should return 3.

# largerthank :: [Int] -> Int -> Int
def largerthank(arr, key):
    l = 0
    u = len(arr) - 1

    while True:
        if l > u:
            p = -1
            break

        m = (l + u) // 2

        if arr[m] < key or arr[m] == key:
            l = m + 1
        else:
            if m > 0:
                if arr[m - 1] <= key:
                    p = m
                    break
                else:
                    u = m - 1
            else:
                p = m
                break
    return p




def bsearch(arr, key):
    l = 0
    u = len(arr) - 1

    while True:
        if l > u:
            p = -1
            break

        m = math.floor((l + u) / 2)

        if arr[m] < key:
            l = m + 1
        elif arr[m] == key:
            p = m
            break
        else:
            u = m - 1

    return p

arr = [1,3,6,9,10,15,18,26,28,36,39,46,60]

# print(bsearch(arr, 60))
print(largerthank(arr, 29))