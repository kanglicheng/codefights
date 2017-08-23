def makeArrayConsecutive2(statues):

    s = sorted(statues[:])
    f = 1
    m = 0

    while f < len(s):
        if s[f] - s[f - 1] > 1:
            m += s[f] - s[f - 1] - 1

        f += 1

    return m
