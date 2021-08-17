from solution import *
from makechange import make_change, generate

import pytest


def exp_func(peopleline):
    bills = {25: 0, 10: 0, 50: 0, 100: 0, 5: 9}  # initial cashbox

    def update_cash(combo):
        for denom in combo:
            if denom in bills:
                bills[denom] -= combo[denom]

    def isChangeAble(options):
        combo = make_change(options, bills)
        if combo:
            update_cash(combo)
            return True
        else:
            return False

    denoms = sorted(bills.keys(), reverse=True)
    waysToMake25 = generate(25, denoms)
    waysToMake75 = generate(75, denoms)

    for bill in peopleline:
        # print (bill, end=",")

        if bill % 30 == 0:
            bills[10] += 3
        else:
            bills[bill] += 1

        if bill is 25:
            continue
        if bill is 30:
            bills[5] -= 1
            if bills[5] < 0:
                return "No"
        if bill is 50:
            if not isChangeAble(waysToMake25):
                return "No"
        if bill is 100:
            if not isChangeAble(waysToMake75):
                return "No"
        # print(bills)  # intermediate cashbox status
    return "Yes"


# @pytest.mark.skip
def test_random_lists():
    '''
    Generates 20 lists of random sizes within
    the range - 5, 10, inclusive.Modify these as per your choice 
    '''
    tcount = 20
    low = -5
    high = 10
    bill_denominations = [25, 25, 25, 30, 30, 50, 100]
    size_variation = [3, 5, 6, 20, 101, 200]

    import random
    bill_dnominations = random.shuffle(bill_denominations)

    for test_num in range(tcount):
        alist = [random.choice(bill_denominations)
                 for count in range(
            random.choice(size_variation)
        )
        ]

        expected = exp_func(alist)
        if len(alist) is 20 or len(alist) is 200:  # and expected == "Yes":
            print(("Test_" + str(test_num), alist, len(alist), exp_func(alist)),
                  end="...\n"
                  )
        else:
            print(("Test_" + str(test_num), len(alist), exp_func(alist)),
                  end="...\n"
                  )
