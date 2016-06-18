
# Sort a linked list

# quick sort and merge sort are possible

import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

def quick_sort_linked_list(node):

    def get_tail(node):
        while node.next:
            node = node.next
        return node

    def partition(head, tail):

        pivot = tail
        prev = None
        curr = head
        new_head = None
        new_tail = tail

        while curr != pivot:
            if curr.data < pivot.data:
                if not new_head:
                    new_head = curr
                prev = curr
                curr = curr.next
            else:
                if prev:
                    prev.next = curr.next
                temp = curr.next
                curr.next = None
                tail.next = curr
                new_tail = curr
                curr = temp

        # if all the elements are larger than the pivot
        # we set new head to the pivot itself
        if not new_head:
            new_head = pivot

        return (new_head, pivot, new_tail)

    def _qs(head, tail):
        if not head or head == tail:
            return head

        new_head, pivot, new_tail = partition(head, tail)

        # if the pivot is smallest element, no need to recurse
        if new_head != pivot:

            # we need to temporarily break the chain between the
            # left partition and the pivot so that we can recurse
            temp = new_head
            while temp.next != pivot:
                temp = temp.next
            temp.next = None

            # after we recurse on the left
            # reattach the two broken portions back
            left_partition_head = _qs(new_head, temp)
            left_partition_tail = get_tail(left_partition_head)
            left_partition_tail.next = pivot

        # recurse on the right partition
        pivot.next = _qs(pivot.next, new_tail)

        return new_head

    _qs(node, get_tail(node))


class TestSuite(unittest.TestCase):
    def test_1(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)

        b.next = a
        a.next = d
        d.next = c

        quick_sort_linked_list(b)

        self.assertEqual(a.next, b)
        self.assertEqual(b.next, c)
        self.assertEqual(c.next, d)

try:
    unittest.main()
except:
    pass
