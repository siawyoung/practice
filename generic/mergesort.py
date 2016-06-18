
def mergesort(arr):

    def merge(a1, a2):

        if not a1:
            return a2

        if not a2:
            return a1


        sorted_a1 = merge(a1[:len(a1) // 2], a1[len(a1) // 2:])
        sorted_a2 = merge(a2[:len(a2) // 2], a2[len(a2) // 2:])

        a1_pointer = 0
        a2_pointer = 0
        output = []

        while a1_pointer < len(sorted_a1) and a2_pointer < len(sorted_a2):
            if sorted_a1[a1_pointer] < sorted_a2[a2_pointer]:
                output.append(sorted_a1[a1_pointer])
                a1_pointer += 1
            else:
                output.append(sorted_a2[a2_pointer])
                a2_pointer += 1

        while a1_pointer < len(sorted_a1):
            output.append(sorted_a1[a1_pointer])
            a1_pointer += 1

        while a2_pointer < len(sorted_a2):
            output.append(sorted_a2[a2_pointer])
            a2_pointer += 1

        return output

    return merge(arr[:len(arr) // 2], arr[len(arr) // 2:])

arr = [2,1,4,1,6,1,2,6,3,0,1,2,6,1,4,2,4]

print(arr)
print(mergesort(arr))