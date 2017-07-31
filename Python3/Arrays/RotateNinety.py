def rotateImage(a):
    print("new image!")
    print(a)
    l = len(a)

    for x in range(l // 2):
        for y in range(x, l - x - 1):
            tmp = a[x][y]
            print("newline:")
            print("t:", x, y)
            print("r:", y, l - x - 1)
            print("b:", l - x - 1, l - y - 1)
            print("l:", l - y - 1, x)

            # switch top for left
            a[x][y] = a[l - y - 1][x]
            # switch left for bottom
            a[l - y - 1][x] = a[l - x - 1][l - y - 1]
            # switch bottom for right
            a[l - x - 1][l - y - 1] = a[y][l - x - 1]
            # switch right for top
            a[y][l - x - 1] = tmp

            #switch
            #a[x][y], a[y][l - x - 1], a[l - x - 1][l - y - 1], a[l - y - 1][x] = a[l - y - 1][x], a[x][y], a[y][l - x - 1], a[l - x - 1][l- y - 1]

    return a


i = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(i))

"""
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
"""

j = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

print(rotateImage(j))

k = [[10,9,6,3,7],
 [6,10,2,9,7],
 [7,6,3,8,2],
 [8,9,7,9,9],
 [6,8,6,8,2]]

print(rotateImage(k))
