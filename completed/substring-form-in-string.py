# You are required to write a method which takes an anonymous letter L and text from a magazine M. Your method is to return true iff L can be written using M, i.e., if a letter appears k times in L, it must appear at least k times in M.

from collections import defaultdict

# matching_letters :: String -> String -> Boolean
def matching_letters(l, m):

    dic = defaultdict(int)
    for i in l:
        dic[i] += 1

    for i in m:
        if dic[i] > 0:
            dic[i] -= 1
        if sum(dic.values()) == 0:
            return True

    return False


l = "abcdefz"
m = "kasjdhfabcdefg"

print(matching_letters(l,m))