
# Design an algorithm for computing the running median of a sequence. The time complexity should be O(logn) per element read in, where n is the number of values read in up to that element


class minHeap:
    def __init__(self):
        self.heapList = [0] # we offset the heap list indices by 1 so that index operations are easier
        self.size = 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i = i // 2

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

   # returns the smaller child of the particular node at i
    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, data):
        self.heapList.append(data)
        self.size += 1
        self.percolateUp(self.size)

    def peek(self):
        return self.heapList[1]

    def removeMin(self):
        _min = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self.percolateDown(1)
        return _min

    def __str__(self):
        return str(self.heapList)

class maxHeap:
    def __init__(self):
        pass

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] > self.heapList[i // 2]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i = i // 2

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    # returns the larger child of the particular node at i
    def maxChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, data):
        self.heapList.append(data)
        self.size += 1
        self.percolateUp(self.size)

    def peek(self):
        return self.heapList[1]

    def removeMax(self):
        _max = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.heapList.pop()
        self.size -= 1
        self.percolateDown(1)
        return _max

    def __str__(self):
        return str(self.heapList)

# To calculate the median, maintain a max heap for the lower half of array, and a min heap for upper half.

# calculate_median_stream :: [Int] -> Int -> Int
def calculate_median_stream(arr, new_item):

    arr = []

    first_half_heap = maxHeap()
    second_half_heap = minHeap()

    # ....
