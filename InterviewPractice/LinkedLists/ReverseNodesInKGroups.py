def reverseNodesInKGroups(l, k):
    prev, nxt, complete = reverseNodes(l, k)

    if not complete:
        prev, nxt, complete = reverseNodes(prev, k)

    if nxt:
        l.next = reverseNodesInKGroups(nxt, k)

    return prev


def reverseNodes(l, k):
    p = None
    c = l
    n = None
    count = 0

    while c and count < k:
        n = c.next
        c.next = p
        p = c
        c = n
        count += 1

    return p, n, count == k
    
