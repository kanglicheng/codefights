def rangeBitCount(a, b):
    return "".join(map(lambda x: bin(x), range(a, b + 1))).count("1")
