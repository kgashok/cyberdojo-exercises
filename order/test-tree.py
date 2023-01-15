from tree import boustrophedon_order, level_order, Node
import pytest


def test_boustro_for_3_levels():

    def array_to_balanced_bst(alist):
        # divide and conquer
        if not alist:
            return
        mid = len(alist) // 2
        root = Node(alist[mid])
        root.left = array_to_balanced_bst(alist[:mid])
        root.right = array_to_balanced_bst(alist[mid + 1:])
        return root

    alist = list(range(1, 16))
    ctree = array_to_balanced_bst(alist)
    print(ctree)

    assert boustrophedon_order(ctree) == [
        8, 12, 4, 2, 6, 10, 14, 15, 13, 11, 9, 7, 5, 3, 1
    ]

    alist = list(range(17))
    ctree = array_to_balanced_bst(alist)
    print(ctree)
    assert boustrophedon_order(ctree) == [
        8, 13, 4, 2, 6, 11, 15, 16, 14, 12, 10, 7, 5, 3, 1, 0, 9
    ]

# @pytest.mark.skip


def test_simple_tree_for_boustrophedon_printing():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    assert boustrophedon_order(root) == [1, 3, 2]


def test_simple_level_order_output():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    assert level_order(root) == [1, 2, 3]


def test_level_order_output(): 
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)

    assert level_order(root) == [1, 3, 2]
