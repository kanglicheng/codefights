def possibleSums(coins, quantity):
    d = {}
    s = []

    for m in range(len(coins)):
        s += [coins[m]] * quantity[m]

    print(s)


    for i in range(1, len(s) + 1):
        for j in comb(s, i):
            t = sum(j)

            if t not in d:
                d[t] = ""

    print(d)
    return len(d)


def comb(lst, ln, cmb = []):
    if len(lst) == ln:
        if cmb.count(lst) == 0:
            cmb.append(lst)

        return cmb

    for i in range(len(lst)):
        rlst = lst[:i] + lst[i + 1:]
        cmb = comb(rlst, ln, cmb)

    return cmb

def permute(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []

    for i in range(len(lst)):
        m = lst[i]
        llst = lst[:i] + lst[i + 1:]

        for p in permute(llst):
            l.append([m] + p)

    return l


#######################################

def possibleSums(coins, quantity):
    d = {}
    sums(coins, quantity, d, 0)
    pass


def sums(coins, quantity, d, s):
    print("location:", coins[0], quantity[0])
    if len(coins) == 1:
        print("end of recursions...", coins[0])
        return coins[0]

    for i in range(len(coins)):
        sums(coins[i + 1:], quantity[i + 1:], d, s)

        if s not in d:
            d[s] = ""

    print(d)
    return len(d)

#######################################

def possibleSums(coins, quantity):
    d = {}


print(possibleSums([10, 50, 100], [1, 2, 1]))
