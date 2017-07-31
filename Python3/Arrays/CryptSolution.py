def isCryptSolution(crypt, solution):
    t = []

    # convert to numbers
    for i in crypt:
        tmp = ""
        for j in i:
            for k in solution:
                if k[0] == j:
                    tmp += k[1]
                    break
        t.append(tmp)

    # see if valid crypto zero
    for m in t:
        if m[0] == "0" and len(m) > 1:
            return False

    # compare addition
    if int(t[0]) + int(t[1]) == int(t[2]):
        return True

    return False


cc = ["SEND", "MORE", "MONEY"]

cs = [['O', '0'],
    ['M', '1'],
    ['Y', '2'],
    ['E', '5'],
    ['N', '6'],
    ['D', '7'],
    ['R', '8'],
    ['S', '9']]

fc = ["TEN", "TWO", "ONE"]

fs = [['O', '1'],
    ['T', '0'],
    ['W', '9'],
    ['E', '5'],
    ['N', '4']]

print(isCryptSolution(cc, cs))
print(isCryptSolution(fc, fs))
