
# In Microsoft Excel, rows are labelled 'A' through 'Z', and then 'AA' to 'ZZ', 'AAA' to 'ZZZ', and so on. Write a function to convert such a label to its actual numerical index (starting from 1, i.e. 'A' should return 1).

import math

def convert(strId):

    cardinality = 26

    starting_pos = 0
    offset = 0

    for i in range(len(strId)):
        starting_pos += math.pow(cardinality, i)

    for index, letter in enumerate(reversed(strId)):
        position = ord(letter) - 65
        offset += math.pow(cardinality, index) * position

    return int(starting_pos + offset)

print(convert('A'))