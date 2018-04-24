def sudoku(grid):
    squares = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [0, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1],

    ]

    positions = [
        [1, 1], [4, 1], [7, 1],
        [1, 4], [4, 4], [7, 4],
        [1, 7], [4, 7], [7, 7]

    ]

    for row in grid:
        hashy = {}
        for square in row:
            if square in hashy:
                return False

            hashy[square] = True

    for column_index in range(len(grid)):
        hashy = {}
        for row_index in range(len(grid)):
            if grid[row_index][column_index] in hashy:
                return False

            hashy[grid[row_index][column_index]] = True


    for position in positions:
        hashy = {}
        for square in squares:
            if grid[position[0] + square[0]][position[1] + square[1]] in hashy:
                return False

            hashy[grid[position[0] + square[0]][position[1] + square[1]]] = True

    return True
