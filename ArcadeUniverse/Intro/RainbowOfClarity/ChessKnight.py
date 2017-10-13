def chessKnight(cell):
    spc = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
    x = ord(cell[0])
    y = int(cell[1])
    moves = 0

    for j in spc:
        if x + j[0] < ord("a") or x + j[0] > ord("h"):
            continue

        if y + j[1] < 1 or y + j[1] > 8:
            continue

        moves += 1

    return moves
