def removeKFromList(l, k):
    if not l:
        return

    prev = l
    curr = l.next

    while curr != None:
        if curr.value == k:
            curr = curr.next
            prev.next = curr
        else:
            prev, curr = curr, curr.next


    if l.value == k:
        l = l.next

    return l
