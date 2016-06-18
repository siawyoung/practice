
# Demonstration of using Python's built-in heap library

import heapq

heap = [0,1,2,3,4,5,6]

heapq.heapify(heap)
print(heapq.heappop(heap))

print(heap)
