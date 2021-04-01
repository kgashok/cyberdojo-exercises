from reversedict import reverse_dict, reverse_dict2
import pytest

pytestmark = pytest.mark.random_order(disabled=True)


def test_reversing_a_simple_dict():
    adict = {1: 2}
    expected = {2: 1}

    assert reverse_dict(adict) == expected


def test_reversing_a_dict_with_two_keys():
    adict = {1: 2, 3: 4}
    expected = {2: 1, 4: 3}
    assert reverse_dict(adict) == expected


def test_reversing_a_dict_containing_char_key_and_number_value():
    adict = {'ajitha': 9000, 'vidhya': 1000}
    expected = {9000: 'ajitha', 1000: 'vidhya'}

    assert reverse_dict(adict) == expected


def test_reversing_a_dict_containing_duplicate_values():
    adict = {'ajitha': 9000, 'vidhya': 9000, 'satish': 2000}
    expected = {9000: ['ajitha', 'vidhya'], 2000: 'satish'}
    assert reverse_dict(adict) == expected


def test_reversing_a_dict_containing_duplicates_values_not_in_order():
    adict = {'vidhya': 9000, 'ajitha': 9000, 'satish': 2000}
    expected = {9000: ['ajitha', 'vidhya'], 2000: 'satish'}
    assert reverse_dict(adict) == expected


def test_reversing_dict_containing_list_as_value():
    adict = {1: 2, 2: [3, 4, 5]}
    expected = {2: 1, 3: 2, 4: 2, 5: 2}
    assert reverse_dict(adict) == expected


def test_reversing_dict_containing_list_as_value_with_duplicates():
    adict = {1: 2, 2: [2, 3, 4, 5]}
    expected = {2: [1, 2], 3: 2, 4: 2, 5: 2}
    assert reverse_dict(adict) == expected


@pytest.mark.parametrize(
    "adict, expected", [
        ({1: 2, 2: [2, 3, 4, 5, 2]},
         {2: [1, 2], 3:2, 4:2, 5:2}),
        ({1: 2, 2: [2, 3, 4], 4:[5, 3, 2]},
         {2: [1, 2, 4], 3: [2, 4], 4:2, 5:4}),
    ]
)
def test_reversing_dict_containing_list_as_value_with_multiple_dups(adict, expected):
    assert reverse_dict(adict) == expected


@pytest.mark.parametrize(
    "adict, expected", [
        ({1: 2, 2: [2, 3, 4, 5, 2]},
         {2: [1, 2, 2], 3:2, 4:2, 5:2}),
        ({1: 2, 2: [2, 3, 4], 4:[5, 5, 3, 2], 100:5},
         {2: [1, 2, 4], 3: [2, 4], 4:2, 5:[4, 4, 100]}),
        ({1: 2, 2: [2, 0, 0, 0, 3], 100:2},
         {2: [1, 2, 100], 0:[2, 2, 2], 3:2}),
    ]
)
def test_reversing_dict_containing_list_as_value_with_multiple_dups(adict, expected):
    assert reverse_dict2(adict) == expected
