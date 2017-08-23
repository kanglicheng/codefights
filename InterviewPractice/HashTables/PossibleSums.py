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
    s = []
    i = 0
    j = 0
    t = 0

    for m in range(len(coins)):
        s += [coins[m]] * quantity[m]

    for p in s:
        d[p] = ""
        t += p

    d[t] = ""

    for n in range(len(s)):
        print("n:", n)
        i = n
        j = 0

        while i < len(s):
            print("{}:".format(i), end = " ")
            j = 0
            t = 0

            while j < len(s):
                if j <= i and j >= i - n:
                    j = i + 1
                    continue

                t += s[j]

                if t not in d:
                    d[t] = 1

                print("{}".format(j), end = " ")

                j += 1

            i += 1


            print()

        print()
        print(d)

    return len(d)

"""
What if you iterated over each new hash table key with the new value?
10, 50, 50, 100

- iterate once over -
a hashtable to know how many {10: 1, 50: 2, 100: 1}
10: 10
50: 50
100: 100

[1, 2, 1]
pretend [1, 1, 1], O(n^2)
for each iterate over the hashtable but not theirself
-ten
60: 10 50
110: 10 100

-fifty
# 60: 50 10
# 100: 50 50
150: 50 100

-hundred
110: 100 10
# 150: 100 50
160: 100 60
210: 100 110
160: 10 50 100
210: 10 50 50 100

iterate again over the hashtable
leftover [0, 1, 0]
# 60: 10 50
# 100: 50 50
# 150: 100 50
# 110: 60 50
# 210: 160 50
260: 210 50

now [0, 0, 0] and we're done. O(n^2) time.
don't worry about "if's". hashtable will just keep them together.

------------
or
- iterate once over -
a hashtable to know how many {10: 1, 50: 2, 100: 1}
10: 10
50: 50
100: 100

-tens
60: 10 50
110: 10 100

-fifty
# 60: 10 50
100: 50 50
150: 50 100
# 110: 60 50
160: 110 50

-fifty once more
# 60: 10 50
# 100: 50 50
# 150: 50 100
# 110: 60 50
# 160: 110 50
# 110: 60 50
# 150: 50 100
# 160: 50 110
210: 50 160

-hundred
# 110: 100 10
# 150: 100 50
# 160: 100 60
200: 100 50 50
...

"""

def possibleSums(coins, quantity):
    d = {}
    p = dict(zip(coins, quantity))

    for c in coins:
        d[c] = {c: 1}

    for q in p:
        for n in range(p[q]):
            for b in list(d):
                if q not in d[b]:
                    d[b + q] = dict(d[b])
                    d[b + q][q] = 1
                    continue

                if d[b][q] < p[q]:
                    d[b + q] = dict(d[b])
                    d[b + q][q] += 1

    print(d)

    return len(d)

#######################################

def possibleSums(coins, quantity):
    d = {}
    p = dict(zip(coins, quantity))

    for c in coins:
        d[c] = {c: 1}

    for q in p:
        for n in range(p[q]):
            for b in list(d):
                if q not in d[b]:
                    d[b + q] = dict(d[b])
                    d[b + q][q] = 1
                    continue

                if d[b][q] < p[q]:
                    d[b + q] = dict(d[b])
                    d[b + q][q] += 1

    return len(d)



#####################################

def possibleSums(coins, quantity):
    d = {}
    p = dict(zip(coins, quantity))

    print(p)

    for c in coins:
        d[c] = ""

    for i in p:
        for j in range(2, p[i] + 1):
            if i * j in d:
                p[i] -= 1

    print(p)





print(possibleSums([10, 50, 100], [1, 2, 1]))
