def secondRightmostZeroBit(n):
    return ~((n + 1)|n) & ((n + 1)|n) + 1
