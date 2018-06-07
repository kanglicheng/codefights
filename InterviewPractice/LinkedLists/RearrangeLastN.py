def rearrangeLastN(l, n):
    if not l:
        return None
    if n == 0:
        return l

    prev = None
    curr = l
    count = 0

    while curr:
        prev = curr
        curr = curr.next
        count += 1

    if count <= n:
        return l

    prev.next = l
    curr = l

    while count > n:
        print(curr.value)
        prev = curr
        curr = curr.next
        count -= 1

    prev.next = None

    return curr
