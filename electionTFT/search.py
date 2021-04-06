def sequential_search(alist, token):
    
    index = 0
    
    while index < len(alist):
        if token == alist[index]:
            return True
        index = index + 1
     
    return False 

def sequential_search(alist, token):
    
    # index = 0
    # while index < len(alist):
    for index in range(len(alist)):
        if token == alist[index]:
            return True
        # index = index + 1
     
    return False 
