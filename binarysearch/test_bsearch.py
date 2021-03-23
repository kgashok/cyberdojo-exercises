from bsearch import binary_search 
import pytest 

pytestmark = pytest.mark.random_order(disabled=True)

def test_finding_5_at_index_2_in_list_containing_1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]   
    assert binary_search(alist, 5) == 2
    assert binary_search([1, 3, 5], 3) == 1 

    
def test_finding_7_at_index_3_in_list_containing__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]    
    assert binary_search(alist, 7) == 3
    
def test_not_finding_2_at_index_2_in_list_containing__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]    
    assert binary_search(alist, 2) == -1

def test_not_finding_10__in_the_list_containing_odd_numbers():
    alist = [1, 3, 5, 7, 9] 
    assert binary_search(alist, 10) == -1 

#@pytest.mark.skip
def test_finding_1_at_index_0_in_list_containing__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]
    assert binary_search(alist, 1) == 0

#@pytest.mark.skip
def test_finding_3_at_index_1_in_list_containing__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]
    
    assert binary_search(alist, 3) == 1
    
