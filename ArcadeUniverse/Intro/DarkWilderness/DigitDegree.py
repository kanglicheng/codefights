def digitDegree(n):
    rnds = 0
    num = str(n)

    while len(num) > 1:
        rnds += 1
        new_num = 0

        for j in num:
            new_num += int(j)

        num = str(new_num)

    return rnds
