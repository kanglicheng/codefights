from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda d, i : d.rotate(i), res, range(0, len(res) * -1, -1)), 0)
    return [list(d) for d in res]
