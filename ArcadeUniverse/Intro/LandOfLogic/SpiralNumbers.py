def spiralNumbers(n):
    grid = [[None for i in range(n)] for j in range(n)]
    drctns = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    dr = 0
    loc = [0, 0]

    for j in range(1, n * n + 1):
        nxt = [loc[0] + drctns[dr][0], loc[1] + drctns[dr][1]]

        if nxt[0] > -1 and nxt[0] < n and nxt[1] > -1 and nxt[1] < n and grid[nxt[1]][nxt[0]] == None:
            grid[loc[1]][loc[0]] = j
            loc = nxt
        else:
            dr = (dr + 1) % len(drctns)
            nxt = [loc[0] + drctns[dr][0], loc[1] + drctns[dr][1]]
            grid[loc[1]][loc[0]] = j
            loc = nxt

    return grid
