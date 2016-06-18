
# Find the second largest item in a binary search tree.

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def __str__(self):
        return str(self.value)

def second_largest(node):
    if not node.left and not node.right:
        return None

    if not node.right:
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr

    prev = node
    curr = node.right

    while curr.right:
        prev = curr
        curr = curr.right

    return prev

a = BinaryTreeNode(6)
b = a.insert_left(3)
c = b.insert_right(4)
d = a.insert_right(8)
e = d.insert_right(10)


print(second_largest(a))


