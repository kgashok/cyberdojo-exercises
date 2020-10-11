from random import shuffle
from duplicate import remove_duplicates


def test_list_with_no_elements():
    arr = []

    assert remove_duplicates(arr) == []


def test_list_with_no_duplicates():
    arr = [1, 2, 3]

    assert remove_duplicates(arr) == [1, 2, 3]


def test_list_with_one_duplicate():
    arr = [1, 1, 2, 3]
    assert remove_duplicates(arr) == [1, 2, 3]

    arr = [100, 100, 4, 3, 2]
    # arr.sort()
    # assert remove_duplicates(arr) == arr

    assert remove_duplicates(arr) == [100, 4, 3, 2]


def test_list_with_lot_of_duplicates():

    arr = list(range(10))
    dup_arr = arr * 2
    li = remove_duplicates(dup_arr)
    assert li == arr

    shuffle(dup_arr)
    assert all([x in li for x in dup_arr])
