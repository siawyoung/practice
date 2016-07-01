
# Given a list of integers, return an integer that appears twice.

# Internally, Python sets are implemented using hash maps, which gives us constant time look up.

def appears_twice(arr):
    s = set()
    for i in arr:
        if i not in s:
            s.add(i)
        else:
            return i

arr = [1,4,8,2,2,4,7,7]

print(appears_twice(arr))

