def isListPalindrome(l):
    if l == None or l.next == None:
        return True

    return are_lists_equal(l, reverse_linked_list(get_middle(l)))


def get_middle(l):
    fast = l
    slow = l

    while fast and fast.next:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    mid = prev

    if fast:
        mid = slow
        slow = slow.next

    return slow


def reverse_linked_list(l):
    p = None
    c = l
    n = None

    while c != None:
        n = c.next
        c.next = p
        p = c
        c = n

    return p


def are_lists_equal(l, l2):
    c1 = l
    c2 = l2

    while c2:
        if c1.value != c2.value:
            return False

        c1 = c1.next
        c2 = c2.next

    return True
