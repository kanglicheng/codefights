def primesSum(a, b):
    return sum(list(filter(lambda x: len([k for k in range(2, int(x ** 0.5) + 1) if x % k == 0]) == 0, [j for j in range(max(2, a), b + 1)])))
