def binary_search(alist, token):

    while alist:
        mid = len(alist) // 2
        midvalue = alist[mid]

        print(f'\nmid:{mid} midvalue:{midvalue}')
        if token == midvalue:
            return True
        if token < midvalue:
            # truncate alist to lower half
            alist = alist[:mid]
        else:
            # truncate alist to upper half
            alist = alist[mid + 1:]

    return False
