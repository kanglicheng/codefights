class Prizes(object):
    def __init__(self, purchases, n, d):
        self.p = iter(enumerate(purchases, 1))
        self.n = n
        self.d = d

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            curr = next(self.p)

            if curr[0] % self.n == 0 and curr[1] % self.d == 0:
                return curr[0]

        raise StopIteration


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
