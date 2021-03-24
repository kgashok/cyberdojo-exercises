def binary_search(alist, token):
    
    while alist: 
        mid = len(alist) // 2
        midvalue = alist[mid] 
    
        if token is midvalue: 
            return True
    
        if token < midvalue: 
            # truncate alist to lower half
            alist = alist[:mid]
        else:
            # truncate to upper half
            alist = alist[mid + 1:]
    
    return False
