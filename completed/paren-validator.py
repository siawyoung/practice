# Let's say:

# '(', '{', '[' are called "openers."
# ')', '}', ']' are called "closers."

# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

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
    def peek(self):
        return self.stack[-1]

def validator(string):
    stack = Stack()
    for i in string:
        if i == '{' or i == '[' or i == '(':
            stack.push(i)
        elif i == '}':
            if stack.peek() != '{':
                return False
            else:
                stack.pop()
        elif i == ')':
            if stack.peek() != '(':
                return False
            else:
                stack.pop()
        elif i == ']':
            if stack.peek() != '[':
                return False
            else:
                stack.pop()

    return True

# string = "{ [ ( ] ) }"
string = "()(){(([]))}"

print(validator(string))

