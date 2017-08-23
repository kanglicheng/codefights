def sudoku2(grid):
    d = 3
    check = [0 for i in range(9)]

    for x in range(len(grid)):
        horz = check[:]
        vert = check[:]
        box = check[:]

        m = (x // d) * d
        p = (x % d) * d

        for y in range(len(grid[x])):
            n = (y // d)
            q = (y % d)

            # check horizontal
            if grid[x][y] != ".":
                horz[int(grid[x][y]) - 1] += 1

            # check vertical
            if grid[y][x] != ".":
                vert[int(grid[y][x]) - 1] += 1

            # check the box
            if grid[m + n][p + q] != ".":
                box[int(grid[m + n][p + q]) - 1] += 1

        for j in range(len(check)):
            if horz[j] > 1 or vert[j] > 1 or box[j] > 1:
                return False

    return True
