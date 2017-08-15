def roadsBuilding(cities, roads):
    mp = []
    nr = []

    for i in range(cities):
        mp.append([])

        for j in range(cities):
                mp[i].append(False)


    for r in roads:
        mp[r[0]][r[1]] = True
        mp[r[1]][r[0]] = True

    for i in range(cities):
        for j in range(cities):
            if i != j and mp[i][j] == False:
                nr.append([i, j])
                mp[i][j] = True
                mp[j][i] = True


    print(mp)
    return nr
