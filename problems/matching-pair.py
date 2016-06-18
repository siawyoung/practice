
# Design an algorithm that takes an abs-sorted array A and a number k, and returns a pair of indices of elements in A that sum up to k. Output (-1, -1) if there is no such pair

# return_abs_pair :: [Int] -> Int -> (Int, Int)

def return_abs_pair(arr, total):

    # there are three cases to consider
    # (+,+)
    # (-,-)
    # (+,-)

    # we try searching for first two cases first
    # by doing a simple (first-last-index) iterative matching

    # this function can be extracted out for standalone use
    # in the case that the sorted array has only positive (or negative) numbers
    def check_using_same_signs(arr, k):

        l = 0
        u = len(arr) - 1

        if k > 0:

            while arr[l] < 0 and l < u:
                l += 1

            while arr[u] < 0 and l < u:
                u -= 1

            while True:
                print(l)
                print(u)
                if l >= u:
                    return (-1,-1)

                _sum = arr[l] + arr[u]
                if _sum == k:
                    return (l,u)
                elif _sum < k:
                    l += 1
                    while arr[l] < 0:
                        l += 1
                else:
                    u -= 1
                    while arr[u] < 0:
                        u -= 1
        else:
            while True:

                if l >= u:
                    return (-1,-1)

                _sum = arr[l] + arr[u]
                if _sum == k:
                    return (l,u)
                elif _sum < k:
                    u -= 1
                    while arr[u] > 0:
                        u -= 1
                else:
                    l += 1
                    while arr[l] > 0:
                        l += 1


    # check for tuples of different signs by starting with
    # the most positive (right-most) integer
    # and the most negative (right-most) integer
    # and iterating leftwards

    # if the current sum is less than the total
    # we move the negative pointer leftwards

    # if the current sum is more than the total
    # we move the positive pointer leftwards
    def check_using_diff_signs(arr, k):

        neg_pointer = len(arr) - 1
        pos_pointer = len(arr) - 1

        while arr[neg_pointer] > 0 and neg_pointer >= 0:
            neg_pointer -= 1

        while arr[pos_pointer] < 0 and pos_pointer >= 0:
            pos_pointer -= 1


        while True:
            # there are either no positive integers or no negative integers
            # the tuple cannot be made up of 1 positive and 1 negative integer
            if neg_pointer <= 0 or pos_pointer <= 0:
                return (-1,-1)

            _sum = arr[neg_pointer] + arr[pos_pointer]

            if _sum == k:
                return (neg_pointer, pos_pointer)

            elif _sum < k:

                neg_pointer -= 1
                while arr[neg_pointer] > 0 and neg_pointer >= 0:
                    neg_pointer -= 1

            else:

                pos_pointer -= 1
                while arr[pos_pointer] < 0 and pos_pointer >= 0:
                    pos_pointer -= 1


    result = check_using_same_signs(arr, total)

    if result != (-1,-1):
        return result

    return check_using_diff_signs(arr, total)

print(return_abs_pair([1,2,-2.5,-3,4,-5],1.5))