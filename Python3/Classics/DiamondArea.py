def shapeArea(n):

    if n == 0:
        return 0

    s = 1
    a = 1

    while s < n:
        s += 1
        a += (s - 1) * 4

    return a

def shapeArea(n):
    if n == 0:
        return 0
        
    return n**2 + (n - 1) ** 2
