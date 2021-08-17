import copy


def make_change(options, cashbox):

    for combo in options:
        for denom in combo:
            if denom not in cashbox or \
                    combo[denom] > cashbox[denom]:
                break
        else:
            return combo

    return None


''' 
var generate25 = [ {25:1}, {5:1, 10:2}, {5:3, 10:1}, {5:5}];
 
var generate75 = [ {25:1, 50:1}, {25:3}, {5:1, 10:7}, 
    {5:1, 10:2, 25:2}, {5:1, 10:2, 50:1}, {5:3, 10:1, 25:2}, 
    {5:3, 10:1, 50:1}, {10:5, 25:1}, {5:15}... 22 combinations ];
 
'''


def maxkey(obj):
    return max(list(obj.keys()))


def generate(money, coins):
    table = {}

    for i in range(1, money+1):
        row = []
        for c in coins:
            if c < i:
                subs = table[i - c]
                for s in subs:
                    sub = copy.deepcopy(s)
                    max = maxkey(sub)
                    if c >= max:
                        sub[c] = sub[c] + 1 if c in sub else 1
                        row.append(sub)
                # end of subs for loop
            elif c == i:
                combo = {}
                combo[c] = 1
                row.append(combo)
        # end of coins loop
        table[i] = row
        # print("table", table[i])
    # end of money loop
    return table[money]
