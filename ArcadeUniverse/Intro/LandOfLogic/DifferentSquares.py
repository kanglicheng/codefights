def differentSquares(matrix):
    squares = []

    for j in range(len(matrix) - 1):
        for k in range(len(matrix[j]) - 1):
            sqr = [matrix[j][k],
                   matrix[j][k + 1],
                   matrix[j + 1][k],
                   matrix[j + 1][k],
                   matrix[j + 1][k + 1]]

            if sqr not in squares:
                squares.append(sqr)

    return len(squares)
