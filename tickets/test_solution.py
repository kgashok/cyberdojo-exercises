from solution import *
 
import pytest
#pytestmark = pytest.mark.skipif()
 
def test_partitioning_of_25_and_75(): 
    print("\nWays to make 25") 
    for i, combo in enumerate(generate(25, [50, 25, 10, 5])):
        print(i, combo)
        
    print("\nWays to make 75")
    for j, combo in enumerate(generate(75, [50, 25, 10, 5])):
        print(j, combo)
        
        
# @pytest.mark.skip
def test_some_line_of_bills(): 
    assert tickets([25, 25, 50, 50, 50, 50]) == "No"     
    assert tickets([25, 50, 25, 100, 25, 50]) == "Yes"
 
 
def test_10_dollar_bills():
    assert tickets([25, 30]) == "Yes"
    
def test_10s_for_servicing_a_100 (): 
    assert tickets([25, 30, 30, 30, 50, 100]) == "Yes"
    
 
def test_20_members_in_line(): 
    assert tickets(
        [30, 30, 25, 25, 30, 25, 100, 25, 25, 25, 25, 25, 50, 25, 25, 25, 30, 25, 30, 30]
    ) == "Yes"

