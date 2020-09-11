from bst import array_to_bst, array_to_balanced_bst, Node, is_valid
# import pytest


def test_full_and_balanced_bst():
    abbst = array_to_balanced_bst([1, 2, 3, 4, 5, 6, 7])
    print(abbst)


def test_for_balanced_bst():
    head = Node(3)
    head.left = Node(1)
    head.left.right = Node(2)
    head.right = Node(4)
    head.right.right = Node(5)
    print(head)

    abbst = array_to_balanced_bst([1, 2, 3, 4, 5])
    print(abbst)
    assert abbst == head

# @pytest.mark.skip


def test_simple_array():

    head = Node(1)
    head.right = Node(2)
    head.right.right = Node(3)

    assert array_to_bst([1, 2, 3]) == head


def test_another_simple_array():

    head = Node(1)
    head.right = Node(2)
    head.right.right = Node(3)
    head.right.right.right = Node(4)
    print(head)

    abst = array_to_bst([1, 2, 3, 4])
    print(abst)
    assert abst == head


def test_another_array_descending_order():
    head = Node(4)
    head.left = Node(3)
    head.left.left = Node(2)
    head.left.left.left = Node(1)
    print(head)

    abst = array_to_bst([4, 3, 2, 1])
    print(abst)
    assert abst == head

    assert(is_valid(abst))
