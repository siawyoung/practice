
#  Write a function that prints the nodes on the exterior of a binary tree in anti-clockwise order, i.e., print the nodes on the path from the root to the leftmost leaf in that order, then the leaves from left-to-right, then the nodes from the rightmost leaf up to the root. For example, when applied to the binary tree in Figure 9.1 on Page 73, your function should return (A,B,C,D,E,H,M,N,P,O,I). (By leftmost (rightmost) leaf, we mean the leaf that appears first (last) in an inorder walk.)

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.right_edge = False

    def __str__(self):
        return str(self.data)

# tree_exterior :: BTreeNode -> void
def tree_exterior(node):

    def _preprocess(node):
        pointer = node
        while pointer:
            if not pointer.right:
                pointer.right_edge = True
                break
            pointer = pointer.right

    def isLeaf(node):
        return not node.left and not node.right

    _preprocess(node)

    curr = node

    while curr:
        print(curr)
        if not curr.left:
            break
        curr = curr.left

    prev = curr
    curr = curr.parent

    while not curr.right_edge:

        if not prev or prev.left == curr or prev.right == curr:
            if curr.left:
                _next = curr.left
            else:
                if isLeaf(curr):
                    print(curr)
                _next = curr.right if curr.right else curr.parent

        elif curr.left == prev:
            if isLeaf(curr):
                print(curr)
            _next = curr.right if curr.right else curr.parent
        else:
            _next = curr.parent


        prev = curr
        curr = _next

    while curr.parent:
        print(curr)
        curr = curr.parent

a = BTreeNode(1)
b = BTreeNode(2)
c = BTreeNode(3)
d = BTreeNode(4)
e = BTreeNode(5)
f = BTreeNode(6)
g = BTreeNode(7)

a.left = b
a.right = c

b.parent = a
c.parent = a

b.left = d
b.right = e

d.parent = b
e.parent = b

c.left = f
c.right = g

f.parent = c
g.parent = c

tree_exterior(a)