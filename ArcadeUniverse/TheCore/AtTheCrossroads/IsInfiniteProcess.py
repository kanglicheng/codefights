def isInfiniteProcess(a, b):
    if b < a:
        return True

    if (b - a) % 2 == 1:
        return True

    return False
