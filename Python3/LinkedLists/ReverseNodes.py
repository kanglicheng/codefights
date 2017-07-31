def reverseNodesInKGroups(l, k):
    # have a start node
    # walk to break and mark break
    # reverse prv list
    # walk to next break
    # repeat until none

    if l is None:
        return None
    if k < 2:
        return l

    s = l
    m = None

    b1 = l
    b2 = l
    b3 = l
    c = 0

    print_ll(b1)

    while b3:
        b1 = b3
        b2 = b3
        b3 = b3

        while c < k:
            if b3 == None:
                break

            b2 = b3
            b3 = b3.next
            c += 1

        b2.next = None

        if c < k:
            if m:
                m.next = b1
            break

        if s == l:
            s = b2
        else:
            m.next = b2

        reverse_list(b1)

        m = b1
        c = 0

    return s


def reverse_list(l):
    p = None
    c = l
    n = None

    while c:
        n = c.next
        c.next = p
        p = c
        c = n

    return p

def print_ll(ll):
    while ll:
        print(ll.value, end = " ")
        ll = ll.next
    print()

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
i = ListNode(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i

print_ll(reverseNodesInKGroups(a, 7))
