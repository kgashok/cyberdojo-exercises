def selection_sort_simple(alist):
    if not alist: 
        return alist
    
    minval = min(alist)
    alist.remove(minval)
    
    return [minval] + selection_sort(alist)


def selection_sort(alist):
    # print(alist)
    if not alist: 
        return alist
    
    try: 
        minval = min(alist) 
    except: 
        for elem in alist: 
            if type(elem) == list: 
                alist.remove(elem)
                alist.extend(elem)
        minval = min(alist)
    finally: 
        alist.remove(minval)
    
    return [minval] + selection_sort(alist)