
# Delete a node from a linked list, given only a reference to the node to be deleted.

# We can mimic a deletion by copying the value of the next node to the node to be deleted, before deleting the next node.

# not a true deletion

class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

    def __str__(self):
        return str(self.value)

def delete_node(node):
    if node.next:
        _next = node.next.next
    else:
        _next = None

    node = node.next
    node.next = _next

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)

print(a)
print(b)