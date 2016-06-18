
# How would you implement a queue given two stacks and 0(1) additional storage? Your implementation should be efficient - the time to do a sequence of m combined enqueues and dequeues should be O(m).

class Stack:
    def __init__(self):
        self._stack = []

    def push(self,data):
        self._stack.append(data)

    def pop(self):
        return self._stack.pop()

    def __len__(self):
        return len(self._stack)

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, data):
        self.inbox.push(data)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.push(self.inbox.pop())

        return self.outbox.pop()

b = Queue()
b.enqueue(1)
b.enqueue(2)

print(b.dequeue())
print(b.dequeue())