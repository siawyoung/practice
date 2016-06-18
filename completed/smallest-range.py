
# You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

# For example,
# List 1: [4, 10, 15, 24, 26]
# List 2: [0, 9, 12, 20]
# List 3: [5, 18, 22, 30]

# The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.



class minHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def swap(self, a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heap[i][0] < self.heap[i // 2][0]:
                self.swap(i, i // 2)
            i = i // 2

    def percolateDown(self, i):
        while i * 2 <= self.size:
            smaller_child_index = self.minChild(i)
            if self.heap[i][0] > self.heap[smaller_child_index][0]:
                self.swap(i, smaller_child_index)
            i = smaller_child_index

    # return the smaller of two children
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            return i * 2 if self.heap[i * 2][0] < self.heap[i * 2 + 1][0] else i * 2 + 1

    def peek(self):
        return self.heap[1]

    def isEmpty(self):
        return self.size == 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.percolateUp(self.size)

    def removeMin(self):
        self.swap(1, self.size)
        _min = self.heap.pop()
        self.size -= 1
        self.percolateDown(1)
        return _min

    def __str__(self):
        return str(self.heap)


# smallest_range :: [[Int]] -> (Int, Int)
def smallest_range(arr):

    heap = minHeap()

    # initialize the heap by adding the first elements of all the arrays in
    for i in range(len(arr)):
        heap.insert([arr[i][0], i])
        arr[i].pop(0)

    start_number = min([ x[0] for x in arr ])
    end_number = max([ x[0] for x in arr ])

    heap_end = end_number

    max_range = end_number - start_number

    while True:

        popped_number = heap.removeMin()

        if not arr[popped_number[1]]:
            break

        next_number_to_add = arr[popped_number[1]].pop(0)

        heap.insert([next_number_to_add, popped_number[1]])

        heap_end = max(heap_end, next_number_to_add)

        curr_difference = heap_end - heap.peek()[0]

        if curr_difference < max_range:
            start_number = heap.peek()[0]
            end_number = heap_end
            max_range = curr_difference

    return (start_number, end_number)

arr = [
    [4,10,15,24,26],
    [0,9,12,20],
    [5,18,22,30]
]

print(smallest_range(arr)) # (20,24)