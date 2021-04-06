from bisect import insort


def insert_into_sorted_array(alist, key, hi=None):
    if not hi:
        hi = len(alist)-1
    return insort(alist, key, hi=hi)


def insert_into_sorted_array(alist, key, index):
    while index > 0 and key < alist[index-1]:
        # alist[index] = alist[index-1]
        index -= 1
    # alist[index] = key
    print("before", alist, key, index)
    alist.insert(index, key)
    print("after", alist)
    # return insort(alist, key, hi=index)


def insert_into_sorted_array(alist, key, index):
    while index > 0 and key < alist[index-1]:
        alist[index] = alist[index-1]
        index -= 1
    alist[index] = key


def insert_into_sorted_array(alist, key, kindex):
    j = kindex
    while j > 0 and key < alist[j-1]:
        j -= 1
    
    if j != kindex:
        # print("\nBefore shift:", alist)
        # shift right by 1 position, (kindex-j) elements
        alist[j+1:kindex+1] = alist[j:kindex]
        # print("After shift:", alist)
        # insert key into the array 
        alist[j] = key
        # print("After insertion", alist)
    

def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        insert_into_sorted_array(alist, key, i)
    return alist
def insertion_sort(alist):
    for i in range(1, len(alist)):
        key = alist[i]
        insert_into_sorted_array(alist, key, i)
    return alist
