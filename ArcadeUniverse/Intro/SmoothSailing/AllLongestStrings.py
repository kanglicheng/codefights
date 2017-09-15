def allLongestStrings(inputArray):
    m = 0
    f = []

    for b in inputArray:
        if len(b) > m:
            m = len(b)

    for j in inputArray:
        if len(j) == m:
            f.append(j)

    return f
