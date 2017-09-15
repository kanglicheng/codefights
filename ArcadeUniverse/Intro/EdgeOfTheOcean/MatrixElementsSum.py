def matrixElementsSum(matrix):
    s = 0

    for m in range(len(matrix[0])):
        for n in range(len(matrix)):
            if matrix[n][m] == 0:
                break

            s += matrix[n][m]

    return s
