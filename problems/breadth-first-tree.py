
# Print the nodes of a tree in breadth-first order.

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

def print_in_level(root):

    queue = [[root, 0]]

    while queue:
        curr = queue.pop(0)
        print(str(curr[0]) + ' level: ' + str(curr[1]) + '\n')
        if curr[0].left:
            queue.append([curr[0].left, curr[1] + 1])
        if curr[0].right:
            queue.append([curr[0].right, curr[1] + 1])


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

print_in_level(a)