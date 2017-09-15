def alternatingSums(a):
    teams = [0, 0]

    for j in range(len(a)):
        teams[j % 2] += a[j]

    return teams
