def chessBoardCellColor(cell1, cell2):
    dx = (ord(cell2[0]) - ord(cell1[0])) % 2
    dy = (ord(cell2[1]) - ord(cell1[1])) % 2

    if dx == dy:
        return True

    return False
