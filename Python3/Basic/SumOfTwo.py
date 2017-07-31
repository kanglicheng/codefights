def sumOfTwo(a, b, v):
    d = {}

    for n in a:
        if abs(n - v) not in d:
            d[abs(n - v)] = ""

    for m in b:
        if m in d:
            return True

    return False
