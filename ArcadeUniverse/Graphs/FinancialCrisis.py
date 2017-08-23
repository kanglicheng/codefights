def financialCrisis(roadRegister):
    l = len(roadRegister)
    f = []
    t = []
    v = []

    for i in range(l):
        t = []

        for j in range(l):
            if i == j:
                continue

            v = []

            for k in range(l):
                if i == k:
                    continue

                v.append(roadRegister[j][k])

            t.append(v)

        f.append(t)

    return f
