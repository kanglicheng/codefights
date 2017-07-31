def matrixElementsSum(matrix):
    s = 0

    for m in range(len(matrix[0])):
        n = 0

        while n < len(matrix):
            if matrix[n][m] != 0:
                print(matrix[n][m])
                s += matrix[n][m]
                n += 1
            else:
                n += 2

    return s


def matrixElementsSum(matrix):
    s = 0

    for m in range(len(matrix) - 1, 0, -1):
        print("level:", m)
        for n in range(len(matrix[m])):
            if matrix[m][n] != 0 and matrix[m - 1][n] != 0:
                print("okay room!", matrix[m][n])
                s += matrix[m][n]

    for p in matrix[0]:
        print("last row")
        if p != 0:
            s += p
        print(n, end = " ")
    print()

    return s

def matrixElementsSum(matrix):
    s = 0

    for m in range(len(matrix[0])):
        n = 0

        while n < len(matrix):
            if matrix[n][m] == 0:
                break

            print(matrix[n][m])
            s += matrix[n][m]
            n += 1
    return s

i = [[0, 1, 1, 2],
[0, 5, 0, 0],
[2, 0, 3, 3]]

j = [[1,1,1,0],
[0,5,0,1],
[2,1,3,10]]

print(matrixElementsSum(i))

# rooms with a 0 are haunted. don't stay above them
