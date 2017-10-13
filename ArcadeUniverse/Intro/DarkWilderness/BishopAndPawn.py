def bishopAndPawn(bishop, pawn):
    dx = ord(pawn[0]) - ord(bishop[0])
    dy = int(pawn[1]) - int(bishop[1])

    if abs(dx) == abs(dy):
        return True

    return False
