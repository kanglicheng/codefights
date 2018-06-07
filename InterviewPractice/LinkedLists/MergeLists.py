def mergeTwoLinkedLists(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 and l2 is None:
        return l1
    if l2 and l1 is None:
        return l2

    if l1.value < l2.value:
        start = l1
    else:
        start = l2

    curr = start
    prev = start

    while l1 and l2:
        if l1.value < l2.value:
            curr = l1
            l1 = l1.next
        else:
            curr = l2
            l2 = l2.next

        prev.next = curr
        prev = prev.next

    if l1:
        prev.next = l1
    if l2:
        prev.next = l2

    return start
