
# Write an efficient function that checks whether any permutation of an input string is a palindrome.

# A linear time solution that uses a boolean hash map that switches on and off for each encounter. At the end, those with True are those with odd number of appearances. In a palindrome, regardless of odd or even length, we can only allow at most 1 character with a odd number of appearances.

from collections import defaultdict

def permutation_palindrome(string):
    hash_map = defaultdict(bool)

    for i in string:
        hash_map[i] = True if not hash_map[i] else False

    odd_one_out = False

    for key in hash_map:
        if hash_map[key]:
            if not odd_one_out:
                odd_one_out = True
            else:
                return False

    return True

string = 'civic'
string = 'ciivc'
string = 'cciva'

print(permutation_palindrome(string))
