def binary_search(alist, token):
    left = 0
    right = len(alist)
    
    while left < right:
        mid = (left + right) // 2
        midvalue = alist[mid]
        if token is midvalue:
            return midvalue
        if token < midvalue:
            right = mid
        else:
            left = mid + 1    
    #print("\nmid", mid, "midvalue", midvalue, "left", left, "right", right)

    # decide 2nd value to compare with
    if mid == len(alist)-1:
        cvalue = alist[-2]
    else: 
        cvalue = alist[mid+1]
    #print("midvalue", midvalue, "cvalue", cvalue)
    
    diff1 = abs(token - midvalue)
    diff2 = abs(token - cvalue)
    if diff1 < diff2: 
        return midvalue
    if diff2 < diff1: 
        return cvalue
    return cvalue if cvalue > midvalue else midvalue
    