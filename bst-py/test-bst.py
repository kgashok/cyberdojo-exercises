from bst import *
import pytest


def test_with_array_to_balanced_bst():
    nlist = list(range(1, 8))

    ctree = array_to_balanced_bst(nlist)

    assert preorder(ctree, []) == [4, 2, 1, 3, 6, 5, 7]


def test_with_a_large_array():
    nlist = list(range(10))


def test_with_simple_sorted_array():

    head = Node(1)
    head.right = Node(2)
    head.right.right = Node(3)

    assert array_to_bst([1, 2, 3]) == head


# @pytest.mark.skip
def test_with_simple_sorted_array_additional():

    head = Node(10)
    head.right = Node(20)
    head.right.right = Node(30)
    head.right.right.right = Node(40)

    assert array_to_bst([10, 20, 30, 40]) == head
    assert array_to_bst([1, 20, 30, 40]) != head


def test_with_descending_values():

    head = Node(4)
    head.left = Node(3)
    head.left.left = Node(2)
    print("test tree", head)

    ctree = array_to_bst([4, 3, 2])
    print("constructed tree", ctree)
    assert is_valid_bst(ctree)

    assert ctree == head
