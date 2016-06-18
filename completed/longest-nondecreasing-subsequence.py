
# Given an array A of nnumbers, find a longest nondecreasing subsequence.

# longest_subsequence :: [Int] -> [Int]
def longest_subsequence(arr):

    longest_subsequence_length = 1
    longest_subsequences_table = [1] * len(arr)
    subsequence = []

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] <= arr[i]:
                longest_subsequences_table[i] = max(longest_subsequences_table[i], longest_subsequences_table[j] + 1)
                longest_subsequence_length = max(longest_subsequence_length, longest_subsequences_table[i])

    for i in range(len(longest_subsequences_table) - 1, 0, -1):
        if longest_subsequences_table[i] == longest_subsequence_length:
            subsequence.append(i)
            longest_subsequence_length -= 1

    return subsequence[::-1]



arr = [3,10,2,4,1,2,1,0,1,5,6,1]
print(arr)
print(longest_subsequence(arr))