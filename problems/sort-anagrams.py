
# Given a list of strings, return a list of lists of strings that groups all anagrams.

# Ex. given {trees, bike, cars, steer, arcs}
# return { {cars, arcs}, {bike}, {trees, steer} }

# m = # of words
# n = length of longest word

# sort all the letters and put it into hash map

from collections import defaultdict

# group_anagrams :: [Str] -> [[Str]]
def group_anagrams(strings):
    hash_map = defaultdict(list)
    for i in strings:
        hash_map[''.join(sorted(i))].append(i)

    return hash_map.values()

arr = ['trees', 'bike', 'cars', 'steer', 'arcs']
print(group_anagrams(arr))

