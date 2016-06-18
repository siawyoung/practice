
# Given an opening parenthesis in a string, find the index of the closing parenthesis.

# Use a stack and keep track of its size. When we reach the position of the opening paren, record the size of the stack, and for future closing paren, check if the stack has gone back to the size of the stack recorded earlier.

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0
    def push(self, item):
        self.stack.append(item)
        self.size += 1
    def pop(self):
        self.size -= 1
        return self.stack.pop()


def find_closing_paren(string, pos):

    stack = Stack()

    for i in range(len(string)):
        if string[i] == '(':

            if i == pos:
                size = stack.size

            stack.push(string[i])

        if string[i] == ')':
            stack.pop()

            if stack.size == size:
                return i


string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

print(find_closing_paren(string, 10))
