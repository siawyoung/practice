
# Write a function that takes as input the root of a binary tree and returns true or false depending on whether the tree is symmetric.

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def symmetric(node):

    if not node.left and not node.right:
        return True

    def _symmetric(left, right):

        if not left or not right:
            return False

        # no children
        if not left.left and not left.right and not right.right and not right.left:
            return True

        if not left.right and not right.left:
            return _symmetric(left.left, right.right)

        if not left.left and not right.right:
            return _symmetric(left.right, right.left)

        if left.left and left.right and right.left and right.right:
            return _symmetric(left.left, right.right) and _symmetric(left.right, right.left)

        return False

    return _symmetric(node.left, node.right)

a = BTreeNode(1)

print(symmetric(a)) # True

b = BTreeNode(2)

a.left = b

print(symmetric(a)) # False

c = BTreeNode(3)

a.right = c

print(symmetric(a)) # True

d = BTreeNode(4)

b.left = d

print(symmetric(a)) # False

e = BTreeNode(5)

c.right = e

print(symmetric(a)) # True

f = BTreeNode(6)

d.right = f

print(symmetric(a)) # False