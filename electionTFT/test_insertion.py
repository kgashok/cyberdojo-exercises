from sort import insertion_sort
import pytest
from random import shuffle

pytestmark = pytest.mark.random_order(disabled=True)


def test_sorted_list_except_element_in_extreme_right():

    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([1, 3, 4, 5, 2]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1, 2, 3, 4, 5, 4.5]) == [1, 2, 3, 4, 4.5, 5]


def test_sorted_list_exception_last_two_elements():

    assert insertion_sort([2, 1, 0]) == [0, 1, 2]
    assert insertion_sort([2, -1, 1]) == [-1, 1, 2]

# @pytest.mark.skip("Random later...")


def test_unsorted_lists():

    test = list(range(40))
    shuffle(test)
    print("random list", test)
    assert insertion_sort(test) == list(range(40))
