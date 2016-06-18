
#  Given a reference to the head of a singly linked list L, how would you determine whether L ends in a null or reaches a cycle of nodes?

class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# we initialize 2 pointers, then send one on double speed
# once they intersect, send one back to the start
# then move them in lock step. The next time they intersect, it will
# be at where the cycle begins
def find_cycles(l1):

    count = 0
    p1 = l1
    p2 = l1

    while True:
        p1 = p1.next
        p2 = p2.next.next
        count += 1
        if p1 == p2:
            break

    # reset one of the pointers back to square 1
    p1 = l1

    while True:
        p1 = p1.next
        p2 = p2.next
        if p1 == p2:
            break

    return p1


a = LinkedNode('a')
b = LinkedNode('b')
c = LinkedNode('c')
d = LinkedNode('d')
e = LinkedNode('e')
f = LinkedNode('f')
g = LinkedNode('g')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = c

print(find_cycles(a))