def lineEncoding(s):
    sub = [[s[0], 0]]

    for j in s:
        if sub[len(sub) - 1][0] != j:
            sub.append([j, 0])

        sub[len(sub) - 1][1] += 1

    encoded = ""

    for k in sub:
        if k[1] > 1:
            encoded += str(k[1]) + k[0]
        else:
            encoded += k[0]

    return encoded
