foundPath = [False]

def hasPathWithGivenSum(t, s):
    if not t and s == 0:
        return True

    reallyHasPathWithGivenSum(t, s)
    return foundPath[0]


def reallyHasPathWithGivenSum(t, s):
    if foundPath[0] == True:
        return

    if not t:
        return False
    if not t.left and not t.right and s - t.value == 0:
        foundPath[0] = True
        return

    reallyHasPathWithGivenSum(t.left, s - t.value)
    reallyHasPathWithGivenSum(t.right, s - t.value)
