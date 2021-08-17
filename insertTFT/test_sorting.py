import random
from sorting import insertion_sort
import pytest
pytestmark = pytest.mark.random_order(disabled=True)


def test_with_three_elements_in_a_list_with_one_element_off():

    test = [10, 9, 11]
    assert insertion_sort(test) == [9, 10, 11]

    # test already sorted list
    test = [9, 10, 11]
    assert insertion_sort(test) == [9, 10, 11]


def test_list_with_three_and_one_off_by_two_positions():

    test = [10, 11, 9]
    assert insertion_sort(test) == [9, 10, 11]


def test_random_list():

    twenty = range(-10, 10)
    test = list(twenty)
    random.shuffle(test)
    assert insertion_sort(test) == list(twenty)
