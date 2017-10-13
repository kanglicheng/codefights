def evenDigitsOnly(n):
    num = str(n)

    for d in num:
        if int(d) % 2 == 1:
            return False

    return True
