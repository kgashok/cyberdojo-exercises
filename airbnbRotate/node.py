try:
    from types import NoneType
except:
    NoneType = type(None)
 
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
    def __repr__(self):
        output = "\n"+str(self.value)
        next = self.next
        while next:
            output += ' -> ' + str(next.value)
            next = next.next
        return output
    
    def __eq__(self, other):
        n1, n2 = self, other
        while type(n1) != NoneType and type(n2) != NoneType:
            if n1.value != n2.value:
                return False
            n1, n2 = n1.next, n2.next
        return type(n1) == NoneType and type(n2) == NoneType
 
def make_linked_list(seq):
    node = None
    while len(seq) > 0:
        item = seq.pop()
        node = Node(item, node)
    return node
