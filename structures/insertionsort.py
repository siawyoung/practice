
def insertionsort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


if __name__ == "__main__":

    arr = [2,4,1,2,6,2,3,1,6]

    print(insertionsort(arr))