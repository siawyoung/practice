

class minHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def swap(a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = self.heap[a]

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                swap(i, i // 2)
                i = i // 2

    def percolateDown(self, i):
        while i * 2 <= self.size:
            smaller_child = self.minChild(i)
            if self.heap[i] > smaller_child:
                swap(i, smaller_child)
                i = smaller_child

    # return the smaller of two children
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            return i * 2 if self.heap[i * 2] < self.heap[i * 2 + 1] else i * 2 + 1

    def peek(self):
        return self.heap[1]

    def removeMin(self):
        _min = self.heap[1]
        swap(1, self.size)
        self.size -= 1
        self.percolateDown(1)
        return _min


