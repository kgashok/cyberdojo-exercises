from bisect import insort


def update(d, k, v):
    if k not in d:
        d[k] = v
    else:
        if type(d[k]) is not list:
            d[k] = [d[k]]
        try:
            # if v is a single value
            insort(d[k], v)
        except TypeError as e:
            # then v must be a list of values
            print(str(e))
            print("-->> Handling list of values...", v)
            for elem in v:
                insort(d[k], elem)


def reverse_dict2(adict):
    res = dict()
    for key, value in adict.items():
        # print(f'key:{key}, value:{value}')
        if type(value) is not list:
            update(res, value, key)
        else:
            ldict = dict()
            for elem in value:
                update(ldict, elem, key)
            # print(f'ldict:{ldict}')
            for k, v in ldict.items():
                update(res, k, v)
        print(f"---> INTER:{res}")

    return res


def reverse_dict(adict):

    res = dict()
    for key, value in adict.items():
        # print(f'\nkey:{key}, value:{value}', end="-->")

        if type(value) is list:
            ldict = dict.fromkeys(value, key)
            # print(f'ldict:{ldict}')
            for key, value in ldict.items():
                update(res, key, value)
            # print(f'res:{res}')
        else:
            update(res, value, key)
        # print(f'res:{res}')

    return res
