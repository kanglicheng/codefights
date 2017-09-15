def isLucky(n):
    ns = str(n)

    if len(str(n)) % 2 == 1:
        return False

    fh = ns[:len(ns) // 2]
    lh = ns[(len(ns) // 2): len(ns) + 1]

    sm1 = 0
    sm2 = 0

    for i in fh:
        sm1 += int(i)

    for j in lh:
        sm2 += int(j)

    if sm1 == sm2:
        return True

    return False
