class Node():
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
    
    # returns the string equivalent of the __repr__() function
    # Refer https://bit.ly/strRepr
    def __str__(self):
        return self.preorder([]).__str__()
    
    # return a list containing values of the pre order traversals
    def preorder(self, alist):
        if not self:
            return alist
        alist.append(self.data)
        if self.left:
            self.left.preorder(alist)
        if self.right:
            self.right.preorder(alist)

        return alist

def printq(q):
    for e in q: 
        print(e)
    print("\n---\n")
        
def boustrophedon_order(root):

    def build_using(first, second):
        if first: 
            res.append(first.data)
            queue.append(first)
        if second:
            res.append(second.data)
            queue.append(second)
            
    res = [root.data]
    queue = [root]
    right_to_left = True
    node_count = 0
    power2 = 2
    while queue:
        #printq(queue)
        node = queue.pop(0)
        if right_to_left:
            build_using(node.right, node.left)           
        else:
            build_using(node.left, node.right)
            
        node_count += 2
        if node_count == power2:
            print("res", res, "nodec", node_count)
            right_to_left = not right_to_left
            node_count = 0
            power2 <<= 1
            queue.reverse()
            
    return res
    
def array_to_balanced_bst(alist):
    # divide and conquer
    alist.sort()
    if not alist:
        return
    mid = len(alist) // 2
    root = Node(alist[mid])
    root.left = array_to_balanced_bst(alist[:mid])
    root.right = array_to_balanced_bst(alist[mid + 1:])

    return root
