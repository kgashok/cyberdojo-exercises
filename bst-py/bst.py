import math


def array_to_balanced_bst(alist):
    # divide and conquer
    if not alist:
        return
    mid = len(alist) // 2
    head = Node(alist[mid])
    head.left = array_to_balanced_bst(alist[:mid])
    head.right = array_to_balanced_bst(alist[mid + 1:])

    return head


def is_valid_helper(node, mini, maxi):
    if not node:
        return True

    if not (mini <= node.data <= maxi):
        return False

    return is_valid_helper(node.left, mini, node.data - 1) and is_valid_helper(
        node.right, node.data + 1, maxi
    )


def is_valid_bst(node):
    return is_valid_helper(node, -math.inf, math.inf)


# return a list containing values of the pre order traversals
def preorder(node, alist):
    if not node:
        return alist
    alist.append(node.data)
    preorder(node.left, alist)
    preorder(node.right, alist)

    return alist


def array_to_bst(alist):

    head = Node(alist[0])
    for number in alist[1:]:
        node = Node(number)
        head.insert(node)

    return head


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

    # Two trees are said to be equivalent if
    #   - the preorder traversals outputs are equal to
    #     each other
    def __eq__(self, other):
        selforder = preorder(self, [])
        otherorder = preorder(other, [])
        # print(selforder, otherorder)
        return selforder == otherorder

        # Returns the preorder traveral values in the tree as a list
        # Refer https://bit.ly/strRepr
        # def __repr__(self):
        alist = preorder(self, [])
        return alist.__str__()

    # returns the string equivalent of the __repr__() function
    # Refer https://bit.ly/strRepr
    def __str__(self):
        return self.__repr__()

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
