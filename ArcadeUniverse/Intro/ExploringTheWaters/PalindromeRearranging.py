def palindromeRearranging(inputString):
    d = {}
    oddball = 0

    for s in inputString:
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1

    for m, n in d.items():
        if n % 2 == 1:
            oddball += 1

        if oddball > 1:
            return False

    return True
