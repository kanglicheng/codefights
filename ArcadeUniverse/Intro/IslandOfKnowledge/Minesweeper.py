def minesweeper(matrix):
    h = len(matrix)
    w = len(matrix[0])
    result = [[0 for a in range(w)] for b in range(h)]

    for j in range(h):
        for k in range(w):
            # top row
            if j - 1 > -1:
                if k - 1 > -1 and matrix[j - 1][k - 1] == True:
                    result[j][k] += 1

                if matrix[j - 1][k] == True:
                    result[j][k] += 1

                if k + 1 < w and matrix[j - 1][k + 1] == True:
                    result[j][k] += 1

            # middle row
            if k - 1 > -1 and matrix[j][k - 1] == True:
                result[j][k] += 1

            # not the middle error

            if k + 1 < w and matrix[j][k + 1] == True:
                result[j][k] += 1

            # bottom row
            if j + 1 < h:
                if k - 1 > -1 and matrix[j + 1][k - 1] == True:
                    result[j][k] += 1

                if matrix[j + 1][k] == True:
                    result[j][k] += 1

                if k + 1 < w and matrix[j + 1][k + 1] == True:
                    result[j][k] += 1

    return result
