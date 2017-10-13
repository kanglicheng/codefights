def differentSymbolsNaive(s):
    d = {}

    for j in s:
        if j not in d:
            d[j] = None

    return len(d)
