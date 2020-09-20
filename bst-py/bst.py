import math


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    # Two trees are equivalent if
    # the preorder traversals outputs are equal
    def __eq__(self, other):
        self_order = self.preorder([])
        other_order = other.preorder([])
        # print(self_order, othe_rorder)
        return self_order == other_order

    # returns the string equivalent of the __repr__() function
    # Refer https://bit.ly/strRepr
    def __str__(self):
        return self.preorder([]).__str__()

    # return a list containing values of the pre order traversals
    def preorder(self, alist):
        if not self:
            return alist
        alist.append(self.data)
        if self.left:
            self.left.preorder(alist)
        if self.right:
            self.right.preorder(alist)

        return alist

    def insert(self, node):
        # determine the parent who will
        # take on the new node as child
        n = self
        while n:
            parent = n
            if node.data < n.data:
                n = n.left
            else:
                n = n.right

        if node.data < parent.data:
            parent.left = node
        else:
            parent.right = node


def array_to_balanced_bst(alist):
    """returns a valid BST containing numbers of a sorted array

    Args:
        alist (list): sorted array containing numbers

    Returns:
        (Node): root node of the constructed balanced BST
    """
    alist.sort()  # just to make sure it is sorted!
    if not alist:
        return
    mid = len(alist) // 2
    root = Node(alist[mid])
    root.left = array_to_balanced_bst(alist[:mid])
    root.right = array_to_balanced_bst(alist[mid + 1:])

    return root


def is_valid_bst(node: Node, mini: int = -math.inf, maxi: int = math.inf):
    """checks whether a tree is a valid binary search tree

    Args:
        node (Node): root
        mini (int, optional): [description]. Defaults to -math.inf.
        maxi (int, optional): [description]. Defaults to math.inf.

    Returns:
        boolean: return True if valid BST, otherwise False
    """
    if not node:
        return True
    if not (mini <= node.data <= maxi):
        return False
    return is_valid_bst(node.left, mini, node.data - 1) and \
        is_valid_bst(node.right, node.data + 1, maxi)


def array_to_bst(alist: list):
    """returns a valid BST containing numbers in the list (aka array)

    Args:
        alist (list): containing list of numbers

    Returns:
        Node: root node of the constructed BST
    """
    root = Node(alist[0])
    for number in alist[1:]:
        node = Node(number)
        root.insert(node)

    return root

