from functools import reduce

def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x, y: x + [x[y] + x[y + 1]], range(n - 2), [0, 1])]
