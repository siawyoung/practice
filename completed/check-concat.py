

# You're given a dictionary of strings, and a key. Check if the key is composed of an arbitrary number of concatenations of strings from the dictionary. For example:

# dictionary: "world", "hello", "super", "hell"
# key: "helloworld" --> return true
# key: "superman" --> return false
# key: "hellohello" --> return true

# We iterate through with a pointer i, then at each i, we iterate backwards from i with a pointer j. If the substring string[j:i + 1] matches a word in the word set, we check if the table[j] is True. If its true, then we set the table entry table[i + 1] to true as well. The table keeps track of which of the prefixes in the string are made up of legal concatenations.

# check_concat :: [Str] -> Str -> Boolean
def check_concat(dic, string):

    word_set = set()

    for i in dic:
        word_set.add(i)

    table = [ False for x in range(len(string) + 1) ]
    table[0] = True

    for i in range(len(string)):
        for j in range(i, -1, -1):
            if string[j:i + 1] in word_set and table[j]:
                table[i + 1] = True

    return table[len(string)]



dic = ["world", "hello", "super", "hell", "he"]

print(check_concat(dic, "helloworld"))
