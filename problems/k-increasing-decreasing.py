
# An array A of n integers is said to be k-increasing-decreasing if elements repeatedly increase up to a certain index after which they decrease, then again increase, a total of k times. Design an efficient algorithm for sorting a k-increasing-decreasing array. You are given another array of the same size that the result should be written to, and you can use O(k) additional storage.

# Modified min heap that compares on the first item in the list
class minHeap:
    def __init__(self):
        self.heapList = [0] # we offset the heap list indices by 1 so that index operations are easier
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def percolateUp(self, i):
        while i // 2 > 0:
            if self.heapList[i][0] < self.heapList[i // 2][0]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i // 2]
                self.heapList[i // 2] = temp
            i = i // 2

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i][0] > self.heapList[mc][0]:
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


# sort_k => [Int] -> [Int]
def sort_k(arr):

    k_positions = []

    curr_k_position = [0]

    for i in range(len(arr) - 2):

        if arr[i] < arr[i+1] and arr[i+1] > arr[i+2]:
            curr_k_position.append(i+1)
            k_positions.append(curr_k_position)
            curr_k_position = [i+2]

        elif arr[i] > arr[i+1] and arr[i+1] < arr[i+2]:
            curr_k_position.append(i+1)
            k_positions.append(curr_k_position)
            curr_k_position = [i+2]

    curr_k_position.append(len(arr) - 1)
    k_positions.append(curr_k_position)

    # all the decreasing arrays are the even ones:
    # [inc, dec, inc, dec...]

    # we reverse all the decreasing arrays
    for i in range(1, len(k_positions), 2):
        l = k_positions[i][0]
        u = k_positions[i][1]

        while True:
            arr[l], arr[u] = arr[u], arr[l]
            l += 1
            u -= 1
            if l >= u:
                break

    heap = minHeap()
    output = []

    # populate initial heap
    # with a list containing the item itself, its position, and the list it belongs to
    for index, positions in enumerate(k_positions):
        heap.insert([arr[positions[0]], positions[0], index])

    # now, empty the heap and populate with a fresh element from the list that the just-removed element belonged to
    while not heap.is_empty():
        _min = heap.removeMin()
        output.append(_min[0])

        if _min[1] < k_positions[_min[2]][1]:
            heap.insert([arr[_min[1] + 1], _min[1] + 1, _min[2]])

    return output

arr = [1,2,3,0,1,2,1]
print(sort_k(arr))