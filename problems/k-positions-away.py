
# The input consists of a very long sequence of numbers. Each number is at most k positions away from its correctly sorted position. Design an algorithm that outputs the numbers in the correct order and uses O(k) storage, independent of the number of elements processed.

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

# approx_sort :: [Int] -> [Int]
def approx_sort(arr, k):
    heap = minHeap()

    for index, num in enumerate(arr):
        if heap.size < k + 1:
            heap.insert(num)
        else:
            arr[index - k - 1] = heap.removeMin()
            heap.insert(num)

    for i in range(-k - 1, 0, 1):
        arr[i] = heap.removeMin()

arr = [1,5,3,7,2,4,6,10,9,8]

approx_sort(arr, 4)

print(arr)
