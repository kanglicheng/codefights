def containsDuplicates(a):
    d = {}

    for c in a:
        if c in d:
            return True
        else:
            d[c] = ""

    return False
