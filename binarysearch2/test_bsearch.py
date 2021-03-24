from bsearch import binary_search
import pytest

def test_finding_5_in_list__1_3_5_7_9(): 
    '''best case of finding in the middle of list'''    
    alist = [1, 3, 5, 7, 9]
    assert binary_search(alist, 5) == True
    
@pytest.mark.skip
def test_not_finding_4_in_list__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]
    assert binary_search(alist, 4) == False 
    
def test_finding_3_in_list__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]
    assert binary_search(alist, 3) == True

def test_finding_7_in_list__1_3_5_7_9():
    alist = [1, 3, 5, 7, 9]
    assert binary_search(alist, 7) == True