
# Find the longest substring that is composed of unique characters.

# longest_unique_substring :: Str -> Str
def longest_unique_substring(string):

    hash_map = {}
    curr_start = 0
    curr_end = 0

    max_start = 0
    max_end = 0

    length = 1

    for i in range(len(string)):
        if string[i] in hash_map:

            if curr_end - curr_start + 1 > length:
                max_start = curr_start
                max_end = curr_end
                length = max_end - max_start + 1

            offending_position = hash_map[string[i]]

            for j in range(curr_start, offending_position + 1):
                del hash_map[string[j]]

            curr_start = offending_position + 1


        hash_map[string[i]] = i
        curr_end += 1

    if curr_end - curr_start > max_end - max_start:
        return string[curr_start : curr_end + 1]
    else:
        return string[max_start:max_end + 1]

    return string[max_start:max_end + 1]

string = 'aabcdabzaqabsaiuergaa' # 'abcd'
string1 = 'a' # 'a'
string2 = 'ab' # 'ab'

print(longest_unique_substring(string))
