
def radix_sort(arr):
    radix = 10
    max_length = False
    placement = 1

    while not max_length:
        max_length = True
        buckets = [ [] for x in range(radix) ]

        for i in arr:
            temp = i // placement
            buckets[temp % radix].append(i)
            if max_length and temp > 0:
                max_length = False

        original_array_index = 0
        for b in range(radix):
            bucket = buckets[b]
            for i in bucket:
                arr[original_array_index] = i
                original_array_index += 1

        print(buckets)
        print(arr)
        placement *= radix

    return arr

def counting_sort(arr,max_score):

    _list = [ 0 ] * (max_score + 1)

    for i in arr:
        _list[i] += 1

    output = []
    for i in range(len(_list)):
        for _ in range(_list[i]):
            output.append(i)

    return output

arr = [1,5,2,1,2,7,3,4,1,3,7,8,2,23,1,9,4,12]

print(counting_sort(arr, 23))

