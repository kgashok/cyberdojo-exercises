from solution import *
from node import make_linked_list
 
import pytest
#pytestmark = pytest.mark.skipif()
 
def test_simple_list_rotate_by_one():
    alist = [5, 6, 7]
    ll = make_linked_list(alist)
    
    assert rotate_linked_list(ll) == make_linked_list([6, 7, 5])
 
def test_simple_list_rotate_by_two():
    alist = [1, 2, 3, 4]
    ll = make_linked_list(alist)
    
    assert rotate_linked_list(ll, 2) == make_linked_list([3, 4, 1, 2])
    
def test_full_rotation():
    alist = [1, 2, 3, 4, 5]
    ll = make_linked_list(alist)
    
    assert rotate_linked_list(ll, 5) == ll
 
def test_odd_list_by_even_shifts():
    alist = [100, 99, 98, 0, 0]
    ll = make_linked_list(alist)
    
    assert rotate_linked_list(ll, 2) == make_linked_list([98, 0, 0, 100, 99])
 
def test_boundary_conditions(): 
    alist = []
    ll = make_linked_list(alist)
    assert rotate_linked_list(ll, 2) == ll 
 
    alist = [100]
    ll = make_linked_list(alist)
    assert rotate_linked_list(ll, 400) == ll
    
def test_alphabets_rotate_twice_but_one():
    import string
    alphabets = string.ascii_lowercase
    alist = list(alphabets)
    ll = make_linked_list(alist)
    assert rotate_linked_list(ll, 51) == \
        make_linked_list(['z'] + list(alphabets[:-1]))
