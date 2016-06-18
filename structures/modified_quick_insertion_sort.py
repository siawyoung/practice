from random import randint
import quicksort
import insertionsort

# a modified version of quick sort that switches to insertion sort once the sub array size goes below 5.

def modified_qs(arr):
    def qs(l,u):
        if u - l > 5:
            insertionsort.swap(arr, l, randint(l,u))
            pivot_value = arr[l]
            m = l
            for i in range(l+1, u+1):
                if arr[i] < pivot_value:
                    m += 1
                    insertionsort.swap(arr, i, m)
            insertionsort.swap(arr, m, l)
            qs(l, m - 1)
            qs(m + 1, u)

    qs(0, len(arr) - 1)
    return arr



def modified_sort(arr):
    modified_qs(arr)
    insertionsort.insertionsort(arr)
    return arr

if __name__ == "__main__":

    arr = [3,1,4,16,34,3,67,1,2,1,0,45,2,21,3,1,5,1,2,4,7,1,3,4,5,1,7,13]
    print(modified_sort(arr))