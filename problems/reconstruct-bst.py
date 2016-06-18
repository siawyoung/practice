
#  Which traversal orders-inorder, preorder, and postorder of a BST can be used to reconstruct the BST uniquely?

# Both preorder and postorder BSTs can be used.

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

# reconstruct -> [Int] -> BTreeNode
def reconstruct(arr):

    if not arr:
        return None

    root = BTreeNode(arr[0])

    m = None
    for i in range(len(arr)):
        if arr[i] > root.data:
            m = i
            break

    # check which part of the array is the left subtree, and which is right subtree
    # by checking which elements are smaller/larger than the root (first element)
    if m:
        print(arr[1:m])
        print(arr[m+1:])
        left_node = reconstruct(arr[1:m])
        right_node = reconstruct(arr[m:])
    else:
        left_node = reconstruct(arr[1:])
        right_node = None

    root.left = left_node
    root.right = right_node

    if left_node:
        left_node.parent = root

    if right_node:
        right_node.parent = root

    return root

pre_arr = [5,2,1,3,9,7,8]

r = reconstruct(pre_arr)
iterativeInOrder(r, print)