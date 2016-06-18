# Given sorted arrays A and B of lengths n and m respectively, return an array C containing elements common to A and B. The array C should be free of duplicates. How would you 'perform this intersection if (1) n << m and (2) n ~= m?

def intersect_sorted(arr1, arr2):
    i = 0
    j = 0

    intersection = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.append(arr1[i])
            temp = arr1[i]
            while i < len(arr1) and arr1[i] == temp:
                i += 1
            while j < len(arr2) and arr2[j] == temp:
                j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return intersection

a = [1,2,5,6,6,6,8,10]
b = [2,4,6,6,10,11,14]

print(intersect_sorted(a,b))