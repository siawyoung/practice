
# Given two nodes in a binary tree T, design an algorithm that computes their lowest common ancestor. Assume that each node has a parent pointer. The tree has n nodes and height h. Your algorithm should run in 0(1) space and O(h) time.

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def lca(node1, node2):

    curr_1 = node1
    curr_2 = node2

    height_1 = 0
    height_2 = 0

    while True:
        curr_1 = curr_1.parent
        height_1 += 1
        if not curr_1.parent:
            break

    while True:
        curr_2 = curr_2.parent
        height_2 += 1
        if not curr_2.parent:
            break


    curr_1 = node1
    curr_2 = node2

    if height_1 > height_2:
        for i in range(abs(height_1 - height_2)):
            curr_1 = curr_1.parent

    else:
        for i in range(abs(height_1 - height_2)):
            curr_2 = curr_2.parent

    while True:
        curr_1 = curr_1.parent
        curr_2 = curr_2.parent

        if curr_1 == curr_2:
            return curr_1

        if not curr_1.parent or not curr_2.parent:
            return None


a = BTreeNode(6)
b = BTreeNode(4)
c = BTreeNode(5)
d = BTreeNode(3)
e = BTreeNode(2)
f = BTreeNode(1)

a.left = b
a.right = c

b.parent = a
b.left = d
b.right = e

c.parent = a
c.left = f

d.parent = b

e.parent = b

f.parent = c

print(lca(d,f))