def groupingDishes(dishes):
    c = {}
    f = []

    for d in dishes:
        for p in range(1, len(d)):
            if d[p] in c:
                c[d[p]][d[0]] = ""
            else:
                c[d[p]] = {}
                c[d[p]][d[0]] = ""

    for b in sorted(c.keys()):
        if len(c[b].keys()) > 1:
            f.append([b] + sorted(c[b].keys()))

    return f
