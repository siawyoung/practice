# You're given an array of integers (eg [3,4,7,1,2,9,8]) Find the index of values that satisfy A+B = C + D, where A,B,C & D are integers values in the array.

# Eg: Given [3,4,7,1,2,9,8] array
# The following
# 3+7 = 1+ 9 satisfies A+B=C+D
# so print (0,2,3,5)

# i use a hash map to record the sums of all the pairs. if indices exist in a key, check if all the indices differ. if they differ, then return them

# quadratic time

from collections import defaultdict

def find_equality(arr):
    hash_map = defaultdict(list)
    for i in range(len(arr)):
        for j in range(i +1, len(arr)):

            # if there are existing indices, check if any of the indices clash
            # if it doesn't clash, we can return it
            if hash_map[arr[i] + arr[j]]:
                indices = hash_map[arr[i] + arr[j]]
                for ind in indices:
                    if ind[0] != i and ind[0] != j and ind[1] != i and ind[1] != j:
                        return (ind, (i,j))

            hash_map[arr[i] + arr[j]].append((i,j))

arr = [3,4,7,1,2,9,8]
print(find_equality(arr))

