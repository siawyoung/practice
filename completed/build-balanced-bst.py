
# How would you build a balanced BST from a sorted array A?

class BTreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

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

def build_bst(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return BTreeNode(arr[0])

    mid = len(arr) // 2

    new_node = BTreeNode(arr[mid])
    new_node.left = build_bst(arr[:mid])
    new_node.right = build_bst(arr[mid+1:])

    if new_node.left:
        new_node.left.parent = new_node

    if new_node.right:
        new_node.right.parent = new_node

    return new_node

arr = [1,4,7,10,13,16,18]
r = build_bst(arr)
iterativeInOrder(r, print)