import random
from selection import selection_sort

import pytest
pytestmark = pytest.mark.random_order(disabled=True)


# @pytest.mark.skipif

@pytest.mark.parametrize(
    "alist, expected", [
        ([], []),
        ([1], [1]),
        ([1, -3], [-3, 1]),
        ([1, -7], [-7, 1]),
        ([1, -7, -9], [-9, -7, 1])
    ]
)
def test_returns_sorted_sample_list(alist, expected):
    assert selection_sort(alist) == expected


@pytest.fixture
def randomlist():
    alst = list(range(10))
    random.shuffle(alst)
    return alst

# @pytest.mark.skipif


@pytest.mark.parametrize(
    "randomlist, expected", [
        (randomlist, list(range(10)))
    ], indirect=["randomlist"]
)
def test_returns_sorted_random_list(randomlist, expected):
    randomlist.extend([0, 8])
    expected = [0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9]
    assert selection_sort(randomlist) == expected


def test_with_nested_lists():
    alist = list(range(10))
    random.shuffle(alist)
    alist.append([12, 11])
    print("test case", alist)

    expected = list(range(10)) + [11, 12]
    assert selection_sort(alist) == expected


def test_with_very_big_list_size():
    '''to cause stack overflow that is typical of recursive functions'''

    alist = list(range(10000))
    random.shuffle(alist)
    assert selection_sort(alist) == list(range(1000))
