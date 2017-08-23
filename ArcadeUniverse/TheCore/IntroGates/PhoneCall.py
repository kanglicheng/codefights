def phoneCall(min1, min2_10, min11, s):
    m = 0

    if min1 <= s:
        s -= min1
        m += 1

    for j in range(9):
        if min2_10 < s:
            s -= min2_10
            m += 1
        else:
            return m

    if min11 < s:
        m += s // min11

    return m
