def areSimilar(a, b):
    cnt = 0

    for j in range(len(a)):
        if a[j] != b[j]:
            cnt += 1

    if cnt > 2:
        return False

    a = sorted(a)
    b = sorted(b)

    for k in range(len(a)):
        if a[k] != b[k]:
            return False

    return True
