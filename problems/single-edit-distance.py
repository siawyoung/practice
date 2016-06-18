

# Given two strings, return boolean True/False, if they are only one edit apart.Edit can be insert/delete/update of only one character in the string.

def only_one_edit_distance(str1, str2):

    if abs(len(str1) - len(str2)) > 1:
        return False

    elif abs(len(str1) - len(str2)) == 1:
        longer_string = str1 if len(str1) > len(str2) else str2
        shorter_string = str2 if longer_string == str1 else str1

        inserted = False

        for i in range(len(shorter_string)):

            if not inserted:

                if longer_string[i] != shorter_string[i]:
                    inserted = True

            else:
                if longer_string[i + 1] != shorter_string[i]:
                    return False

        return True if not inserted else False
    else:

        modified = False

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if not modified:
                    modified = True
                else:
                    return False


        return modified

print(only_one_edit_distance('xyaz', 'zyb'))
