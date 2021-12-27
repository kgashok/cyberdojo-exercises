import pytest
from validate import validate


def test_for_valid():
    '''if 79927398713 then return VALID'''
    assert validate(79927398713) == "VALID"
    assert validate(79927398713) == "VALID"
    assert validate(513467882132) == "VALID"


# @pytest.mark.skip
def test_for_invalid_and_3_as_correct_check_digit():
    '''if 79927398716 then return INVALID 3'''
    assert validate(79927398716) == "INVALID 3"


def test_for_invalid_and_2_as_correct_check_digit():
    '''if 513467882134 then return INVALID 2'''

    assert validate(513467882134) == "INVALID 2"
