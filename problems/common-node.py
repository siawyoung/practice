
#  Let h1 and h2 be the heads of lists L1 and L2, respectively. Assume that L1 and L2 are well-formed, that is each consists of a finite sequence of nodes. (In particular, neither list has a cycle.) How would you determine if there exists a node r reachable from both h1 and h2 by following the next fields? If such a node exists, find the node that appears earliest when traversing the lists. You are constrained to use no more than constant additional storage.

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

# find_overlap :: LinkedNode -> LinkedNode -> LinkedNode
def find_overlap(l1, l2):
    length_l1 = 0
    length_l2 = 0

    # first check if they even overlap
    # and count length
    curr_l1 = l1
    curr_l2 = l2
    while True:
        length_l1 += 1
        if curr_l1.next:
            curr_l1 = curr_l1.next
        else:
            break

    while True:
        length_l2 += 1
        if curr_l2.next:
            curr_l2 = curr_l2.next
        else:
            break

    if curr_l1 != curr_l2:
        return False

    # reset the pointers
    curr_l1 = l1
    curr_l2 = l2

    if length_l1 > length_l2:
        for i in range(abs(length_l1 - length_l2)):
            curr_l1 = curr_l1.next
    else:
        for i in range(abs(length_l1 - length_l2)):
            curr_l2 = curr_l2.next

    while curr_l1 != curr_l2:
        curr_l1 = curr_l1.next
        curr_l2 = curr_l2.next

    return curr_l1

a = LinkedNode('a')
b = LinkedNode('b')
c = LinkedNode('c')
d = LinkedNode('d')
e = LinkedNode('e')
f = LinkedNode('f')
g = LinkedNode('g')

a.next = b
b.next = c
c.next = f
d.next = e
e.next = f
f.next = g

print(find_overlap(a,d))