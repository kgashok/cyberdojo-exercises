from search import sequential_search
import pytest

pytestmark = pytest.mark.random_order(disabled=True)

def test_finding_token_sequentially_in_a_list():
    assert sequential_search([1, 2, 3, 4], 1) is True 
    
def test_finding_token_not_in_list_should_returns_false():
    assert sequential_search([1, 2, 3, 4], 0) is False 

def test_finding_token_not_in_first_position():
    '''finding token not in the first position'''
    assert sequential_search([1, 2, 3, 4], 2) is True 
    assert sequential_search([1, 2, 3, 4], 3) is True 

