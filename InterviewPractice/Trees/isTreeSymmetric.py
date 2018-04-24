def isTreeSymmetric(t):
    if t == None:
        return True

    return isReallySymmetric(t.left, t.right)

def isReallySymmetric(l, r):
    if not l and not r:
        return True
    if not l:
        return False
    if not r:
        return False

    if l.value != r.value:
        return False

    return isReallySymmetric(l.left, r.right) and isReallySymmetric(l.right, r.left)
