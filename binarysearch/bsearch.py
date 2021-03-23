def binary_search(alist, token): 
    # initialize markers at the edges of the list 
    left = 0
    right = len(alist) - 1
    
    while left <= right: 
        mid = (left + right) // 2
        midvalue = alist[mid]
        
        #print(f'left:{left} right:{right} mid:{mid} midval:{midval}')
        if midvalue == token:
            print("Token", token, "Found at", mid)
            return mid
        
        if token > midvalue:
            # if token is 7 and midval is 5...
            # shift left marker to the right of mid
            left = mid + 1
        else: # if token < midvalue
            right = mid - 1
    
    print("Token", token, "Not found!")
    return -1 

