def calcFinalScore(scores, n):
    gen = (x * x for x in reversed(sorted(scores)))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
