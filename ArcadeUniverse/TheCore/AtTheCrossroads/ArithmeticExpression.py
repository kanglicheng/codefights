def arithmeticExpression(a, b, c):
    if a > c:
        a, c = c, a

    return True if a + b == c or a * b == c else False
