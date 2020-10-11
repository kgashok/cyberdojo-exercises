# from collections import OrderedDict


def remove_duplicates_inplace(seq):
    """

    :param seq: array of numbers

    """
    seen = {}
    pos = 0
    for item in seq:
        if item not in seen:
            seen[item] = True
            seq[pos] = item
            pos += 1
    del seq[pos:]


def remove_duplicates(alst):
    """

    :param alst: list of numbers

    """
    # from stackoverflow
    return [
        item
        for pos, item in enumerate(alst)
        if alst.index(item) == pos
    ]

    # suggested by BA
    # overhead of creating a dictionary and then converting
    # to a list
    # adict = dict()
    # return list(adict.fromkeys(alst))

    # suggested by Tarun
    # will not maintain order
    # costly because of sorting
    # return sorted(list(set(alst)))

    # the normal iterative code
    # by Dayanand, improved by Sagar
    '''
    nlst = []
    for elem in alst:
        if elem not in nlst:
            nlst.append(elem)
    return nlst
    '''

    # suggested by Sagar
    # nlst = [i for j, i in enumerate(alst) if i not in alst[:j]]
    '''
    nlst = [
        elem
        for pos, elem in enumerate(alst)
        if elem not in alst[:pos]
    ]
    return nlst
    '''

    # nlst = list(OrderedDict.fromkeys(alst))
    # return nlst

    # in-place removal of duplicates by Suveksha
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
