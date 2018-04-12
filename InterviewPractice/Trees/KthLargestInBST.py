kv = [0, None]

def kthSmallestInBST(t, k):
    if t == None:
        return 0

    if kv[1]:
        return kv[1]

    kthSmallestInBST(t.left, k)

    kv[0] += 1
    if kv[0] == k:
        kv[1] = t.value

    kthSmallestInBST(t.right, k)
    
    return kv[1]
