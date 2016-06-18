# Write a function kth_to_last_node() that takes an integer k and the head_node of a singly linked list, and returns the  kth to last node in the list.

# We can do this in a single pass. With 2 pointers, have one pointer move k positions ahead, then move both in tandem until one reaches the end.

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

def kth_to_last_node(node, k):
    if not node:
        return
    if not node.next:
        return node if k == 1 else None

    first_pointer = node
    second_pointer = node

    for i in range(k):
        second_pointer = second_pointer.next

    while second_pointer.next:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next

    return first_pointer

class TestSuite(unittest.TestCase):
    def test_1(self):

        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(kth_to_last_node(a, 2), b)

unittest.main()