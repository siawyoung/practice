
# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
#  A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

# We do it recursively - base case is [0] when we reach a leaf node, and going up, we add + 1 height all entries

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


def check_balance(node):

    def _calculate_height(node):
        if not node.left and not node.right:
            return [0]
        elif not node.right:
            return [ x + 1 for x in _calculate_height(node.left)]
        elif not node.left:
            return [ x + 1 for x in _calculate_height(node.right)]
        else:
            return [ x + 1 for x in _calculate_height(node.left)] + [ x + 1 for x in _calculate_height(node.right)]

    leaf_heights = _calculate_height(node)

    # if any of the leaves deviate by more than 1, then its not superbalanced
    for i in leaf_heights:
        if i > leaf_heights[0] + 1 or i < leaf_heights[0] - 1:
            return False

    return True

a = BinaryTreeNode(1)
b = a.insert_left(2)
c = a.insert_right(3)
d = b.insert_left(1)
e = d.insert_left(1)
g = c.insert_left(1)

print(check_balance(a))


