
# in place shuffle of a list

# inspired from programming pearls

import random

def shuffle(arr):
    for i in range(len(arr)):
        r = random.randint(0, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]

    return arr

arr = [1,2,3,4,5,6,7,8,9]
print(shuffle(arr))
