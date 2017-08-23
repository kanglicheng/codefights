def rotateImage(a):
    l = len(a)

    for x in range(l // 2):
        for y in range(x, l - x - 1):
            tmp = a[x][y]
            
            # switch top for left
            a[x][y] = a[l - y - 1][x]
            # switch left for bottom
            a[l - y - 1][x] = a[l - x - 1][l - y - 1]
            # switch bottom for right
            a[l - x - 1][l - y - 1] = a[y][l - x - 1]
            # switch right for top
            a[y][l - x - 1] = tmp

    return a
