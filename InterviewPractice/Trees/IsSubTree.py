def isSubtree(t1, t2):
    if not t2:
        return True

    return hasSubtree(t1, t2)


def hasSubtree(t1, t2):
    if t1 and not t2:
        return False
    if not t1 and t2:
        return False
    if not t1 and not t2:
        return True

    if t1.value == t2.value:
        return hasSubtree(t1.left, t2.left) and hasSubtree(t1.right, t2.right)
    else:
        return hasSubtree(t1.left, t2) or hasSubtree(t1.right, t2)
