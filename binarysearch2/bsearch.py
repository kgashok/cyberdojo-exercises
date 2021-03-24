def binary_search(alist, token):
    while alist:
        mid = len(alist) // 2
        midvalue = alist[mid]

        if token is midvalue:
            return True

        if token < midvalue:
            # throw/slice away upper half
            alist = alist[:mid]
        else:
            # throw/slice away lower half
            alist = alist[mid + 1:]
    return False
