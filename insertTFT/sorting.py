# list method heavy code
def insertion_sort(alist):

    for i in range(1, len(alist)):
        key = alist.pop(i)
        while i and key < alist[i-1]:
            i = i - 1
        alist.insert(i, key)

    return alist


def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        j = i
        while j and key < alist[j-1]:
            # alist[j] = alist[j-1]
            j = j - 1
        alist[j+1:i+1] = alist[j:i]  # right shift by 1
        alist[j] = key

    return alist
