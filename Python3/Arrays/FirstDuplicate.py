def first_duplicate(a):
    for n in a:
        if a[abs(n) - 1] > 0:
            a[abs(n) - 1] *= -1
        else:
            return abs(n)

    return -1


first_duplicate([1, 2, 3])
print(first_duplicate([1, 2, 2, 3]))
print(first_duplicate([2, 3, 3, 5, 7, 2]))
