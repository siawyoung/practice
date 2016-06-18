
# Given two strings, represented as arrays of characters A and B, compute the minimum number of edits needed to transform the first string into the second string.

# tabulate a table

def edit_distance(str_a, str_b):

    shorter_string = str_a if len(str_a) < len(str_b) else str_b
    longer_string = str_b if shorter_string == str_a else str_a

    table = [ x for x in range(len(shorter_string) + 2) ]

    for i in range(len(longer_string)):

        new_table = [None] * (len(shorter_string) + 1)

        for j in range(-1, len(shorter_string)):

            if j == -1:
                new_table[j + 1] = i + 1
                continue

            if longer_string[i] == shorter_string[j]:

                new_table[j + 1] = table[j]

            else:

                new_table[j + 1] = 1 + min(new_table[j], table[j], table[j + 1])

        table = new_table

    return table[-1]

str_1 = 'Oreed'
str_2 = 'Orchestra'

print(edit_distance(str_1, str_2))


