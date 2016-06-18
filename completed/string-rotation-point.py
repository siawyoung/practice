
# Write a function for finding the index of the "rotation point," which is where I started working from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we want to be efficient here.


# use binary search

# the key here is that, to know which direction to iterate into, compare the current mid with the last item in the currently-considered list

# for eg. 8 9 1 2 3 4 5 6 7
# arr[m] = 3
# since 3 < 7, we look left

# for say, 3 4 5 6 7 8 9 1 2
# arr[m] = 7
# since 7 < 2, we look right

def find_rotation_point(arr):
    assert len(arr) > 0
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]

    l = 0
    u = len(arr) - 1

    while l <= u:

        m = (l + u) // 2

        # the case when the array is not rotated at all
        if m == 0:
            return 0

        if arr[m] < arr[m - 1]:
            return m

        if arr[m] < arr[u]:
            u = m - 1

        else:
            l = m + 1

    # it shouldn't reach here unless the input is not valid
    return None

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'zzz',
    'zzzzz',
    'zzzzzzz',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

print(find_rotation_point(words))