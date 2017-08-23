def arithmeticExpression(a, b, c):
    if a > c:
        a, c = c, a

    if a + b == c:
        return True

    if a * b == c:
        return True

    return False
