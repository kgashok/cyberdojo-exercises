def binary_search(alist, token):
    while alist:
        mid = len(alist) // 2
        midvalue = alist[mid]

        if token is midvalue:
            return True
        if token < midvalue:
            # for e.g. token is 3, and midvalue is 5
            # throw/slice away the upper half
            alist = alist[:mid]
        else:
            # if token is 7, and midvalue is 5
            # throw/slice away the lower half
            alist = alist[mid + 1:]

    return False


def binary_search(alist, token):
    while alist:
        mid = len(alist) // 2
        midvalue = alist[mid]

        if token is midvalue:
            return True

        alist = alist[:mid] if token < midvalue else \
            alist[mid+1:]
    return False
