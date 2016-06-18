
# Let L = (l(0)...l(n-1)) be a sequence. Define even-odd(L} to be the sequence (l(0), l(2)....l(1), l(3)...), i.e., the elements at even indices followed by the elements at odd indices.

# Write a function that takes a singly linked list L, and reorders the elements of L so that the new list represents even-odd(L). Your function should use 0(1) additional storage. The only field you can change is `next`.

class LinkedNode:
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

# even_odd :: LinkedNode -> Maybe(LinkedNode)
def even_odd(start):

    if not start:
        return None

    if not start.next:
        return start

    even_pointer = start
    odd_pointer = start.next
    first_odd = start.next

    while True:
        if not even_pointer.next or not even_pointer.next.next or not odd_pointer.next or not odd_pointer.next.next:

            if even_pointer.next and even_pointer.next.next:
                even_pointer.next = even_pointer.next.next
                even_pointer = even_pointer.next

            odd_pointer.next = None
            even_pointer.next = first_odd
            break

        even_pointer.next = even_pointer.next.next
        even_pointer = even_pointer.next

        odd_pointer.next = odd_pointer.next.next
        odd_pointer = odd_pointer.next

    return start


a = LinkedNode(0)
b = LinkedNode(1)
c = LinkedNode(2)
d = LinkedNode(3)
e = LinkedNode(4)
f = LinkedNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

even_odd(a)
print(a.print_all())
