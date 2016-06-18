
#  Write a program to test whether the letters forming a string s can be permuted to form a palindrome. For example, "edified" can be permuted to form "deified". Explore solutions that trade time for space.


# assume all lower case letters

# palindrome :: String -> Boolean
def palindrome(str):
    bitmap = [0] * 26
    str_list = [ ord(i) - 97 for i in str ]
    for i in str_list:
        bitmap[i] = 1 if bitmap[i] == 0 else 0
    return sum(bitmap) <= 1

print(palindrome('edified'))
