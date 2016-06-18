
# Write a function condense_meeting_times() that takes a list of meeting time ranges and returns a list of condensed ranges.

# The strategy is put all the meeting time tuples into a min heap, then pull out the min, and then keep pulling out tuples whose starting time is less than the current ending time. Whenever a later ending time is encountered, it is updated. Once no such tuple exist, we append the current starting and ending time to the output, and start again.

class minHeap:
    def __init__(self):
        self.heap = [None]
        self.size = 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heap[i][0] < self.heap[i // 2][0]:
                self.swap(i, i // 2)
            i = i // 2

    def percolateDown(self, i):
        while i * 2 <= self.size:
            mc = self._minChild(i)
            if self.heap[i][0] > self.heap[mc][0]:
                self.swap(i, mc)
            i = mc

    def swap(self, a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def _minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        if self.heap[i * 2][0] > self.heap[i * 2 + 1][0]:
            return i * 2 + 1
        return i * 2

    def peek(self):
        return self.heap[1]
    def isEmpty(self):
        return self.size == 0

    def removeMin(self):
        self.swap(1, self.size)
        _min = self.heap.pop()
        self.size -= 1
        self.percolateDown(1)
        return _min

    def insert(self, i):
        self.heap.append(i)
        self.size += 1
        self.percolateUp(self.size)

    def __str__(self):
        return str(self.heap)

# condense_meeting_times :: [(Int, Int)] -> [(Int, Int)]
def condense_meeting_times(times):
    heap = minHeap()

    for i in times:
        heap.insert(i)

    output = []

    while not heap.isEmpty():
        curr_start, curr_end = heap.removeMin()
        while not heap.isEmpty() and heap.peek()[0] <= curr_end:
            _, curr_end = heap.removeMin()

        output.append((curr_start, curr_end))

    return output

arr =   [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
print(condense_meeting_times(arr))

