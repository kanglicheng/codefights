def correctLineup(athletes):
    return [athletes[k] for j in range(1, len(athletes), 2) for k in range(j, j - 2, -1)]
