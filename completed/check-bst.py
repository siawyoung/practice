
# Check if a binary tree is a BST:

# check :: BTreeNode -> Boolean

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def check(node):

    def _check(node, _min, _max):

        if not node:
            return True

        return node.data > _min and node.data < _max and _check(node.left, _min, node.data) and _check(node.right, node.data, _max)


    return _check(node.left, float('-inf'), node.data) and _check(node.right, node.data, float('inf'))

a = BTreeNode(2)
b = BTreeNode(1)
c = BTreeNode(3)
d = BTreeNode(1.5)

a.left = b
a.right = c

b.parent = a
b.right = d

c.parent = a

d.parent = b

print(check(a))