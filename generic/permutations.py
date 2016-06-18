
import pdb

def permutations(iterable, _range=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

    # all possible candiates
    candidates = tuple(iterable)
    length = len(candidates)

    # width of output
    _range = length if _range is None else _range

    if _range > length:
        return

    # list of all indices
    indices = list(range(length))

    cycles = list(range(length, length - _range, -1))

    yield tuple(candidates[i] for i in indices[:_range])

    while length:
        for i in reversed(range(_range)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = length - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(candidates[i] for i in indices[:_range])
                break
        else:
            return

# The algorithm is:

# Remove the first letter
# Find all the permutations of the remaining letters (recursive step)
# Reinsert the letter that was removed in every possible location.
# The base case for the recursion is a single letter. There is only one way to permute a single letter.

# Worked example

# Imagine the start word is bar.

# First remove the b.
# Find the permuatations of ar. This gives ar and ra.
# For each of those words, put the b in every location:
# ar -> bar, abr, arb
# ra -> bra, rba, rab

def recursive_permutation(word):

    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms = permutations(word[1:])
    char = word[0]
    result = []

    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm) + 1):
            result.append(perm[:i] + tuple(char) + perm[i:])

    return result

for s in recursive_permutation('abc'):
    print(s)