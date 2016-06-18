
# Design an efficient algorithm to compute the diameter of a tree.

# A tree must have a root. The diameter of a tree is the combined length of its 2 longest branches.

# Modified class with any number of children
class TreeNode:
    def __init__(self):
        self.parent = None
        self.children = []

    def add_child(self, node, weight):
        self.children.append([node, weight])
        node.parent = self

    def __str__(self):
        return str(self.data)

def diameter(root):

    def longest_branch(node):
        if not node.children:
            return 0
        return max([child[1] + longest_branch(child[0]) for child in node.children])

    main_branches = [child[1] + longest_branch(child[0]) for child in root.children]
    return sum(sorted(main_branches)[-2:])

a = TreeNode()
b = TreeNode()
c = TreeNode()
d = TreeNode()
e = TreeNode()
f = TreeNode()
g = TreeNode()

h = TreeNode()

a.add_child(b, 2)
a.add_child(c, 9)

b.add_child(d, 1)
b.add_child(e, 3)

d.add_child(h, 3)

c.add_child(f, 7)
f.add_child(g, 8)

print(diameter(a))