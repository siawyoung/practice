
# Define a node in a binary tree to be k-balanced if the difference in the number of nodes in its left and right subtrees is no more than k.

# Design an algorithm that takes as input a binary tree and positive integer k, and returns a node u in the binary tree such that u is not k-balanced, but all of u's descendants are k-balanced. If no such node exists, return null.

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def k_unbalanced(node, k):

    def _k(node):

        if not node:
            return 0

        if not node.left and not node.right:
            return 1

        left_result = _k(node.left)
        right_result = _k(node.right)

        if isinstance(left_result, int) and isinstance(right_result, int):
            if abs(left_result - right_result) > k:
                return node
            else:
                return left_result + right_result + 1

        elif not isinstance(left_result, int):
            return left_result

        else:
            return right_result

    result = _k(node)

    if isinstance(result, int):
        return None

    return result

a = BTreeNode(1)
b = BTreeNode(2)
c = BTreeNode(3)
d = BTreeNode(4)
e = BTreeNode(5)
f = BTreeNode(6)
g = BTreeNode(7)
h = BTreeNode(8)

a.left = b
a.right = c
c.right = d
d.right = e
c.left = f

b.left = g
g.left = h

print(k_unbalanced(a, 2))