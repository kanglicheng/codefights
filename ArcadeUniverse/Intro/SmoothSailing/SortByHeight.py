def sortByHeight(a):
    s = []
    index = 0

    for j in a:
        if j != -1:
            s.append(j)

    s = sorted(s)

    for k in range(len(a)):
        if a[k] != -1:
            a[k] = s[index]
            index += 1

    return a
