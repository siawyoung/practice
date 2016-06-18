

# You are given a set of unique characters and a string.

# Find the smallest substring of the string containing all the characters in the set.

# ex:
# Set : [a, b, c]
# String : "abbcbcba"

# Result: "cba"

from collections import defaultdict

def smallest_substring(char_set, string):
    hash_map = defaultdict(int)
    tail = 0
    current_fulfilled_count = 0

    minimum_string_length = float('inf')

    for i in range(len(string)):
        if string[i] in char_set:

            if hash_map[string[i]] == 0:
                current_fulfilled_count += 1

            hash_map[string[i]] += 1

        while current_fulfilled_count == len(char_set):

            # if current length shorter than minLength:
            if i - tail + 1 < minimum_string_length:
                minimum_string_length = i - tail + 1
                result = string[tail: i + 1]

            # then, we attempt to chop off the tail and see if that
            # decreases the current fulfilled count
            hash_map[string[tail]] -= 1
            if hash_map[string[tail]] == 0:
                current_fulfilled_count -= 1

            tail += 1

    return result

print(smallest_substring(['a', 'b', 'c'], 'abbcbcba'))
