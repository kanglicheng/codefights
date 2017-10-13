from itertools import permutations

def stringsRearrangement(inputArray):
    m = make_map(inputArray)

    perm = list(permutations(inputArray))

    for p in perm:
        b = True

        for j in range(len(p) - 1):
            if p[j + 1] not in m[p[j]]:
                b = False
                break

        if b == True:
            return True

    return False



def make_map(a):
    d = {}

    for j in a:
        d[j] = []

        for k in a:
            b = 0

            if j != k:
                for m in range(len(j)):
                    if j[m] != k[m]:
                        b += 1

                if b == 1:
                    d[j].append(k)

    return d
