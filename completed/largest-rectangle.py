
#  Let A be an array of n numbers encoding the heights of adjacent buildings of unit width. Design an algorithm to compute the area of the largest rectangle contained in this skyline.

# largest_rectangle :: [Int] -> Int
def largest_rectangle(arr):

    stack = []

    left_indices = []
    right_indices = []

    for i  in range(len(arr)):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        left_indices.append(-1 if not stack else stack[-1])
        stack.append(i)

    # empty the stack for the right pass

    stack = []

    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        right_indices = [len(arr) if not stack else stack[-1]] + right_indices
        stack.append(i)

    max_area = 0
    for i in range(len(arr)):
        max_area = max(max_area, arr[i] * (right_indices[i] - left_indices[i] - 1))

    return max_area



if __name__ == "__main__":
    arr = [4,0,4,4,5,5,0,1]
    print(largest_rectangle(arr))

