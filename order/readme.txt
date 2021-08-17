Good morning! Here's your coding interview problem for today.

This problem was asked by Morgan Stanley.

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].


---

- How to simplify the problem? 
- Go from Known To Unknown? 
   - Level Order before we do Boustro ( ITERATIVE)
       - BREADTH FIRST 
         - queue (list) 
            - q.pop(0) -> deque
            - q.append(elem) -> enqueue
       
   -  compared to preorder, postorder, inorder (DEPTH FIRST) 
       - normally you use recursion 
          - stack
          
          