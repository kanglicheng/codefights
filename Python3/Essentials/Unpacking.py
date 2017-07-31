def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a, *res, a = res
    return res
