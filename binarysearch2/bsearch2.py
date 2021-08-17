def binary_search(alist, token):
    left = 0
    right = len(alist)

    while left < right:
        mid = (left + right) // 2
        midvalue = alist[mid]
        # print(f'\nmid:{mid}, midvalue:{midvalue}')
        if token is midvalue:
            return mid

        if token < midvalue:
            # move right marker to left of mid
            right = mid
        elif token > midvalue:
            # move left marker to right of mid
            left = mid+1

    return -1
