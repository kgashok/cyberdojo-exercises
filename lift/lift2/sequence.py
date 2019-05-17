def generate(n):

    out = [2]
    start = out[0]

    for i in range(1, n):
        start += start + (i % 2 if i % 2 == 1 else -1)
        out.append(start)

    print(out)

    return out
