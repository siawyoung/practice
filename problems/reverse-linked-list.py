
# Give a linear time non-recursive function that reverses a singly linked list. The function should use no more than constant storage beyond that needed for the list itself.

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# reverse :: LinkedNode -> LinkedNode
def reverse(node):

    if not node.next:
        return node

    back_pointer  = node
    front_pointer = node.next

    while front_pointer:
        temp = front_pointer.next
        front_pointer.next = back_pointer
        back_pointer.next = None

        back_pointer = front_pointer
        front_pointer = temp

    return back_pointer


# None -> None
# [0] -> [0]
# [0,1] -> [1,0]
# etc

a = LinkedNode(1)
b = LinkedNode(2)
c = LinkedNode(3)
d = LinkedNode(4)

a.next = b
b.next = c
c.next = d

print(reverse(a))
