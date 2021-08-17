from random import shuffle
from duplicate import remove_duplicates, remove_duplicates_inplace


def test_list_with_no_elements():
    """ """
    arr = []
    assert remove_duplicates(arr) == []


def test_list_with_no_duplicates():
    """ """
    arr = [1, 2, 3]
    assert remove_duplicates(arr) == [1, 2, 3]


def test_list_with_one_duplicate():
    """ """
    arr = [1, 1, 2, 3]
    assert remove_duplicates(arr) == [1, 2, 3]

    arr = [100, 100, 4, 3, 2]
    assert remove_duplicates(arr) == [100, 4, 3, 2]


def test_list_with_lot_of_duplicates():
    """ """

    arr = list(range(10))
    dup_arr = arr * 2
    li = remove_duplicates(dup_arr)
    assert li == arr

    shuffle(dup_arr)
    assert all([x in li for x in dup_arr])


def test_for_inplace_remove_of_duplicates_from_SO():
    """ """
    lst = [8, 8, 9, 9, 7, 15, 15, 2, 20, 13, 2, 24, 6, 11, 7, 12, 4, 10, 18,
           13, 23, 11, 3, 11, 12, 10, 4, 5, 4, 22, 6, 3, 19, 14, 21, 11, 1,
           5, 14, 8, 0, 1, 16, 5, 10, 13, 17, 1, 16, 17, 12, 6, 10, 0, 3, 9,
           9, 3, 7, 7, 6, 6, 7, 5, 14, 18, 12, 19, 2, 8, 9, 0, 8, 4, 5]

    remove_duplicates_inplace(lst)

    assert lst == [
        8, 9, 7, 15, 2, 20, 13, 24, 6, 11, 12, 4, 10, 18, 23, 3, 5, 22, 19, 14,
        21, 1, 0, 16, 17
    ]
