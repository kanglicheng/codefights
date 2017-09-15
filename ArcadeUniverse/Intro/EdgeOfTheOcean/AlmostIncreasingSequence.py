def almostIncreasingSequence(sequence):
    if len(sequence) == 2:
        return True

    d = []

    for i in range(1, len(sequence)):
        if sequence[i - 1] >= sequence[i]:
            d.append(i - 1)

    if len(d) == 0:
        return True

    if len(d) == 1:
        if d[0] == 0 or d[0] == len(sequence) - 2:
            return True
        if sequence[d[0] - 1] <  sequence[d[0] + 1]:
            return True
        if sequence[d[0]] < sequence[d[0] + 2]:
            return True

    return False
