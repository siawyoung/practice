

# Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted.
# Example, for this input string


# @"the boy ran"
# the output would be


# @"eht yob nar"
# Tell the complexity of the solution.

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

def reverse_words(string):


    stack = Stack()
    output = []

    for i in range(len(string)):
        if string[i] == ' ':
            while not stack.isEmpty():
                output.append(stack.pop())
            output.append(' ')
        else:
            stack.push(string[i])

    while not stack.isEmpty():
        output.append(stack.pop())

    return ''.join(output)

print(reverse_words('the boy ran'))


