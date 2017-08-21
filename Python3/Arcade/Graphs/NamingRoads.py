def namingRoads(roads):
    d = {}

    if len(roads) == 1:
        return True

    if len(roads) == 2:
        return False
    
    for r in roads:
        d[r[2]] = [r[0], r[1]]

    for i in range(2, len(roads)):
        if d[i - 2][0] in d[i - 1] or d[i - 1][0] in d[i]:
            return False

        if d[i - 2][1] in d[i - 1] or d[i - 1][1] in d[i]:
            return False

    return True
