def almostIncreasingSequence(sequence):
    q = 0
    m = 2

    if len(sequence) < 3:
        return True

    while m < len(sequence):
        if sequence[m - 2] >= sequence[m]:
            q += 1

        if sequence[m - 2] >= sequence[m - 1]:
            if sequence[m] <= sequence[m - 1]:
                q += 1

        m += 1

    if q > 1:
        return False

    return True


def almostIncreasingSequence(sequence):
    if len(sequence) < 3:
        return True

    q = 0

    pv = sequence[0]
    mx = sequence[1]

    if sequence[0] > sequence[1]:
        pv, mx = mx, pv
        q += 1

    for m in range(1, len(sequence)):
        print("step:", sequence[m - 1], sequence[m])
        if sequence[m - 1] >= sequence[m] and sequence[m - 1] <= pv:
            q += 1

        if sequence[m] > mx:
            pv = mx
            mx = sequence[m]

    print("pv, mx:", pv, mx)
    print("q:", q)

    if q > 1:
        return False

    return True


def almostIncreasingSequence(sequence):
    if len(sequence) < 3:
        return True

    m = 2
    q = 0

    pv = sequence[0]
    mx = sequence[1]

    if sequence[0] >= sequence[1]:
        print("step")
        pv, mx = mx, pv
        q += 1
    """
    #m = 0
    #pv = -1000000
    #mx = -1000000

    for m in range(2, len(sequence)):
        print("pv, max:", pv, mx)
        if sequence[m] > mx:

            pv = mx
            mx = sequence[m]
        elif sequence[m] > pv:
            print('step')
            mx = sequence[m]
            q += 1
        else:
            print('step')
            q += 1
    ###
    """
    while m < len(sequence):
        if sequence[m] > mx:
            pv = mx
            mx = sequence[m]
        elif sequence[m] > pv:
            print("step")
            mx = sequence[m]
            q += 1
        else:
            print("step")
            q += 1

        m += 1

def almostIncreasingSequence(sequence):
    if len(sequence) < 3:
        return True
    print()
    print(sequence)

    q = 0

    pv = sequence[0]
    mx = sequence[0]

    if sequence[0] >= sequence[1]:
        #print("first is big")
        pv = sequence[1]
        mx = sequence[1]
        q += 1

    for m in range(3, len(sequence)):
        #print("l, m, n", sequence[m - 2], sequence[m - 1], sequence[m])
        if mx < sequence[m - 2]:
            #print("new max")
            pv = mx
            mx = sequence[m - 1]

        if pv < sequence[m - 2]:
            #print("new prev")
            pv = sequence[m - 2]

        if sequence[m] <= pv or sequence[m - 2] >= sequence[m]:
            q += 1

        #print("pv, mx:", pv, mx)

    print("pv, mx:", pv, mx)
    #print("q:", q)

    return q < 2

def almostIncreasingSequence(sequence):
    if len(sequence) < 2:
        return True

    f = 0
    l = len(sequence) - 1
    q = 0

    pv = sequence[f]
    mx = sequence[l]

    if mx < pv:
        pv, mx = mx, pv

    print()
    print(sequence)

    while f < l and q < 2:
        print("f, l:", sequence[f], sequence[l])
        print("min, max", pv, mx)

        if sequence[l] > mx:
            pv = mx
            mx = sequence[l]

        if sequence[f] >= sequence[l]:
            q += 1
        elif sequence[l] == pv or sequence[f] == pv:
            q += 1

        f += 1
        l -= 1


    #print("min, max", pv, mx)
    #print("q:", q)

def almostIncreasingSequence(sequence):
    if len(sequence) < 2:
        return True

    q = 0

    t = 0
    h = 1
    l = 2

    if sequence[t] > sequence[h]:
        t += 1
        h += 1
        l += 1
        q += 1

    if sequence[t] > sequence[h]:
        h += 1
        q += 1

    print()
    print(sequence)

    while l < len(sequence):
        print("t, h, l:", sequence[t], sequence[h], sequence[l])
        if sequence[h] < sequence[l]:
            
        t += 1
        h += 1
        l += 1

        if h - t > 3 or q > 2:
            return False

        if q > 2:
            return False


    return q < 2

a = [1, 1, 1, 2, 3]
b = [10, 1, 2, 3, 4, 5]
c = [1, 2, 1, 2]
d = [1, 3, 2, 1]
e = [3, 5, 67, 98, 3]
f = [1, 2, 3, 10, 8]
g = [10, 1, 2, 3, 4, 5, 4]
h = [1, 2, 3, 4, 3, 6]
i = [10, 1, 2, 3, 4, 5, 6, 1]
j = [1, 2, 3, 4, 99, 5, 6]

print(almostIncreasingSequence(j))
#print(almostIncreasingSequence(b))
#print(almostIncreasingSequence(c))
#print(almostIncreasingSequence(d))
#print(almostIncreasingSequence(e))
#print(almostIncreasingSequence(f))
#print(almostIncreasingSequence(g))
#print(almostIncreasingSequence(h))
