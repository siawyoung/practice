
# Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

# O(2n) solution

from collections import defaultdict

def find_unique_integer(arr):
    hash_map = defaultdict(int)
    for i in arr:
        hash_map[i] += 1
    print(hash_map)
    for k in hash_map:
        if hash_map[k] == 1:
            return k

arr = [4,5,2,1,5,1,1,6,1,3,1,2,3,4,2]
print(find_unique_integer(arr))
