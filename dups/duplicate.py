from collections import OrderedDict
def remove_duplicates(alst):
    return [ 
        item
        for pos, item in enumerate(alst)
        if alst.index(item) == pos
    ]

    #adict = dict()
    #return list(adict.fromkeys(alst))

    #return sorted(list(set(alst)))
    
    '''
    nlst = []
    for elem in alst: 
        if elem not in nlst: 
            nlst.append(elem)
        
    return nlst 
    '''
    
    #nlst = [i for j, i in enumerate(alst) if i not in alst[:j]]
    '''
    nlst = [
        elem for idx, elem in enumerate(alst) 
        if elem not in alst[:idx]
    ]
    return nlst 
    '''
    
    #nlst = list(OrderedDict.fromkeys(alst))
    #return nlst

    #alst[:] = OrderedDict.fromkeys(alst)
    #return alst
    

    '''
    alst.sort()
    for i in range(len(alst)-1): 
        count = 0 
        for j in range(i+1, len(alst)-1): 
            if alst[i] == alst[j]: 
                count += 1
        if count != 0: 
            for j in range(count): 
                for k in range(i, len(alst)-1): 
                    alst[k] = alst[k+1]
                if j == 0: 
                    del alst[len(alst)-1:]
                else: 
                    del alst[len(alst)-j:]
        i += count 
        
    return alst 
    '''                
                    
                    
                
                
