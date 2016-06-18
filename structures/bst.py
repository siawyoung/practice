class BSTreeNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


    def max(self):
        curr = self
        while True:
            if not curr.right:
                return curr
            curr = curr.right

    def min(self):
        curr = self
        while True:
            if not curr.left:
                return curr
            curr = curr.left

    # the successor of a node can be determined as follows:
    # if the node has a right child, then the successor is the
    # minimum element in the right subtree
    # if not, then, we keep looking up until the current node
    # is a left child of its parent
    # if we reach the root without having found such a condition
    # then the node is the largest element (right-most) node of the tree
    # in which case we simply return the original node
    def successor(self):
        if self.right:
            return self.right.min()

        curr = self
        while True:
            if not curr.parent:
                return None
            if curr == curr.parent.left:
                return curr.parent
            curr = curr.parent

    # the predecessor is similar to the successor, except in reverse
    # if the node has a left child, then the predecessor is the
    # maximum element in the left subtree
    # if its not, then we keep looking until the current node
    # is the right child of its parent, in which case the parent is the predecessor
    # if we reach the root without having found such a condition
    # then the node is the smallest element (left-most) node of the tree
    # in which case we simply return the original node
    def predecessor(self):
        if self.left:
            return self.left.max()

        curr = self
        while True:
            if not curr.parent:
                return None
            if curr == curr.parent.right:
                return curr.parent
            curr = curr.parent

class BSTree:
    def __init__(self, root = None):
        self.root = root

    def insert(self, key):
        new_node = BSTreeNode(key)

        if not self.root:
            self.root = new_node
            return new_node

        # find the correct place for the new node
        curr = self.root
        while True:
            if new_node.key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    new_node.parent = curr
                    return new_node
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    new_node.parent = curr
                    return new_node
                else:
                    curr = curr.right

    def search(self, key):
        curr = self.root
        while True:
            if curr.key == key:
                return curr

            if key < curr.key:
                if not curr.left:
                    return None
                curr = curr.left
            else:
                if not curr.right:
                    return None
                curr = curr.right

    # TODO
    def remove(self, key):
        removing_node = self.search(key)
        if not removing_node:
            return None


    # copied from MIT
    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

tree = BSTree()

tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(4)
tree.insert(1.2)
tree.insert(0)
tree.insert(2.5)
tree.insert(1.5)

print(tree)
a = tree.search(1.5)
print(a)
print(a.successor())
print(a.predecessor())