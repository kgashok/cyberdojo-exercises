from tree import boustrophedon_order, array_to_balanced_bst, Node

def test_simple_tree_for_boustrophedon_printing():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    assert boustrophedon_order(root) == [1, 3, 2]
    

def test_with_height_of_three():
    
    alist = [1, 2, 3, 4, 5, 6, 7]
    ctree = array_to_balanced_bst(alist)
    
    print(ctree.preorder([]))
    
    assert boustrophedon_order(ctree) == [4, 6, 2, 1, 3, 5, 7]
    
def test_with_random_tree():
    pass