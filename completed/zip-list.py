# Write a function that takes a singly linked list L, and reorders the elements of L to form a new list representing zip(L). Your function should use 0(1) additional storage. The only field you can change in a node is next.

# e.g. given a list 1 2 3 4 5, it should become 1 5 2 4 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def print_all(self):
        curr = self
        while True:
            print(curr)
            if curr.next:
                curr = curr.next
            else:
                break

def zip(node):

    temp = node
    temp1 = node.next

    if not temp1:
        return node

    current_end = None
    current_pointer = node

    while True:

        while True:
            if current_pointer.next is current_end:
                break
            current_pointer = current_pointer.next

        current_end = current_pointer

        temp.next = current_end
        current_end.next = temp1

        if temp1.next is current_end:
            temp1.next = None
            break

        temp = temp1
        temp1 = temp1.next

        current_pointer = temp

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e

zip(a)

a.print_all()