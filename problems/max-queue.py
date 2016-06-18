
# Implement a constant time max() operation for a Queue class.

class MaxQueue:
    def __init__(self):
        self.queue = []
        self.deque = []

    def enqueue_front_deque(self, item):
        self.deque = [item] + self.deque

    def dequeue_front_deque(self):
        return self.deque.pop(0)

    def enqueue_back_deque(self, item):
        self.deque.append(item)

    def dequeue_back_deque(self):
        return self.deque.pop()

    def enqueue(self, item):

        self.queue.append(item)

        if item > self.max():
            self.enqueue_front_deque(item)
        else:

            while True:
                pointer = self.deque[-1]
                if pointer > item:
                    self.enqueue_back_deque(item)
                    break
                else:
                    self.dequeue_back_deque()


    def dequeue(self):
        item = self.queue.pop(0)
        if item == self.max():
            self.dequeue_front_deque()
        return item

    def max(self):
        if not self.deque:
            return float('-inf')
        return self.deque[0]


a = MaxQueue()

a.enqueue(4)
a.enqueue(2)
a.enqueue(3)

print(a.max())
a.dequeue()
print(a.max())
a.dequeue()
print(a.max())
a.enqueue(5)
print(a.max())
a.enqueue(1)
print(a.max())
a.enqueue(3)
print(a.max())
a.dequeue()
print(a.max())