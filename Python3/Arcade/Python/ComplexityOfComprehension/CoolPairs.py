def coolPairs(a, b):
    uniqueSums = { i + j for i in a for j in b if not (i * j) % (i + j)}
    return len(uniqueSums)
