
# Implement a constant time max() function on a stack.

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, data):
        if not self._stack:
            self._stack.append([data, data])
        else:
            new_max = max(self.max(), data)
            self._stack.append([data, new_max])

    def pop(self):
        return self._stack.pop()[0]

    def peek(self):
        return self._stack[-1][0]

    def max(self):
        return self._stack[-1][1]