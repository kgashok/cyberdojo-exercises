def has_fixed(alst):
    """

    :param alst:

    """
    maxindex = len(alst) - 1
    for index, val in enumerate(alst):
        if val > maxindex:
            break
        if index == val:
            return index

    return False


def bin_search(alst, op):
    """

    :param alst:
    :param op:

    """
    high = len(alst)-1
    low = 0

    while low <= high:
        mid = low + (high - low)//2
        print(op, ":", low, high, mid, alst[mid])

        if alst[mid] == mid and \
            (mid-1 != -1 and alst[mid-1] != mid-1 or
             mid+1 != len(alst) and alst[mid+1] != mid+1):
            return mid
        if op == 'gt':
            if alst[mid] > mid:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if alst[mid] > mid:
                low = mid + 1
            else:
                high = mid - 1
    return False


def has_fixed(alst):
    """

    :param alst:

    """
    res = bin_search(alst, "lt")
    if not res:
        return bin_search(alst, "gt")
    return res
