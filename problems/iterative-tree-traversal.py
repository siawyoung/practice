 # Let T be the root of a binary tree in which nodes have an explicit parent field. Design an iterative algorithm that enumerates the nodes inorder and uses 0(1) additional space. Your algorithm cannot modify the tree.

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

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

def iterativeInOrder(root, func):
    if not root:
        return

    prev = None
    curr = root
    _next = None

    while curr:
        if not prev or prev.left == curr or prev.right == curr:
            if curr.left:
                _next = curr.left
            else:
                func(curr)
                _next = curr.right if curr.right else curr.parent

        elif curr.left == prev:
            func(curr)
            _next = curr.right if curr.right else curr.parent
        else:
            _next = curr.parent

        prev = curr
        curr = _next

def iterativePreOrder(root, func):
    if not root:
        return

    prev = None
    curr = root
    _next = None

    while curr:
        if not prev or prev.left == curr or prev.right == curr:
            func(curr)
            if curr.left:
                _next = curr.left
            else:
                _next = curr.right if curr.right else curr.parent
        elif curr.left == prev:
            _next = curr.right if curr.right else curr.parent
        else:
            _next = curr.parent
        prev = curr
        curr = _next

def iterativePostOrder(root, func):
    if not root:
        return

    prev = None
    curr = root
    _next = None

    while curr:
        if not prev or prev.left == curr or prev.right == curr:
            if curr.left:
                _next = curr.left
            elif curr.right:
                _next = curr.right
            else:
                func(curr)
                _next = curr.parent
        elif curr.left == prev:
            if curr.right:
                _next = curr.right
            else:
                func(curr)
                _next = curr.parent
        else:
            func(curr)
            _next = curr.parent
        prev = curr
        curr = _next

iterativeInOrder(a, print)
iterativePreOrder(a, print)
iterativePostOrder(a, print)