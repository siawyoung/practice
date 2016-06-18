
# If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings.

# For example:
# Input: "1123". You need to general all valid alphabet codes from this string.

# Output List
# aabc //a = 1, a = 1, b = 2, c = 3
# kbc // since k is 11, b = 2, c= 3
# alc // a = 1, l = 12, c = 3
# aaw // a= 1, a =1, w= 23
# kw // k = 11, w = 23

def alphabet_code(string):

    assert len(string) > 0

    for i in string:
        assert int(i) > 0 and int(i) <= 26

    def consult(substr):
        return chr(int(substr) + 96)

    output = []

    for i in range(len(string)):

        print(output)

        curr = []
        if i == 0:
            curr.append(consult(string[i]))
            output.append(curr)
            continue

        for j in output[i - 1]:
            curr.append(j + consult(string[i]))

        if consult(string[i - 1] + string[i]):

            if i == 1:
                curr.append(consult(string[i - 1] + string[i]))
            elif i > 1:
                for j in output[i - 2]:
                    curr.append(j + consult(string[i - 1] + string[i]))

        output.append(curr)

    return output[-1]




string = '11111'

print(alphabet_code(string))
