def first_duplicate(a):
    for n in a:
        if a[abs(n) - 1] > 0:
            a[abs(n) - 1] *= -1
        else:
            return abs(n)

    return -1
