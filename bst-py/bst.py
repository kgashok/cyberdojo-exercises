
import math


def array_to_balanced_bst_helper(alist, low, high, root):
    if low > high:
        return root

    mid = low + (high - low) // 2

    root = Node(alist[mid])

    root.left = array_to_balanced_bst_helper(alist, low, mid - 1, root.left)
    root.right = array_to_balanced_bst_helper(alist, mid + 1, high, root.right)

    return root


def array_to_bbst(alist):

    return array_to_balanced_bst_helper(alist, 0, len(alist) - 1, None)


class Node():

    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    # if the preorder traversals are the same,
    # then the BSTs are the same
    def __eq__(self, other):
        selfrep = self.preorder(self, [])
        otherrep = other.preorder(other, [])
        return selfrep == otherrep

    # has to be a string object
    def __repr__(self):
        alist = []
        self.preorder(self, alist)
        return alist.__str__()

    def __str__(self):
        return self.__repr__()

    def preorder(self, node, alist):
        if not node:
            return alist
        alist.append(node.data)
        if node.left:
            self.preorder(node.left, alist)
        if node.right:
            self.preorder(node.right, alist)
        return alist


def is_valid_helper(node, mini, maxi):
    if not node:
        return True

    if not (mini <= node.data <= maxi):
        return False
    return is_valid_helper(node.left, mini, node.data - 1) and \
        is_valid_helper(node.right, node.data + 1, maxi)


def is_valid(node):
    return is_valid_helper(node, -math.inf, math.inf)


def array_to_bst(alist):
    if not alist:
        return Node(None)

    head = Node(alist[0])
    node = head
    for i, e in enumerate(alist[1:]):
        parent = None
        while node:
            parent = node
            if e < node.data:
                node = node.left
            else:
                node = node.right
        if e < parent.data:
            parent.left = Node(e)
        else:
            parent.right = Node(e)

        node = head

    return head
