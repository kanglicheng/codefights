from itertools import combinations_with_replacement, product

def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return sorted(list(filter(lambda x : float(x) % d == 0, map(createNumber, product(digits, repeat=k)))))
