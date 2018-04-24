def calkinWilfSequence(number):
    def fractions():
        prev, curr = None, [1, 1]

        while True:
            yield curr

            prev = curr
            curr = [prev[1], 2 * (prev[0] - prev[0] % prev[1]) + prev[1] - prev[0]]



    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
