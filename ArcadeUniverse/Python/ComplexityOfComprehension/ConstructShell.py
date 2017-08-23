def constructShell(n):
    return [[0 for i in range(j)] for j in range(1, n + 1)] + [[0 for i in range(j)] for j in range(n - 1, 0, -1)]
