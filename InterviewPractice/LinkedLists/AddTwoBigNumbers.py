# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def addTwoHugeNumbers(a, b):
    if a is None and b is None:
        return None

    if a and b is None:
        return b

    if b and a is None:
        return b

    a = reverse_list(a)
    b = reverse_list(b)

    f = None
    p = None
    c = a
    d = b
    r = 0

    while c or d:
        n = ListNode(0)

        if p is None:
            f = n
        if p:
            p.next = n
        if c:
            n.value += c.value
        if d:
            n.value += d.value

        n.value += r

        if n.value >= 10000:
            r = n.value // 10000
            n.value -= 10000
        else:
            r = 0

        if c:
            c = c.next
        if d:
            d = d.next

        p = n


    if r > 0:
        p.next = ListNode(r)
        print(p.next.value)

    f = reverse_list(f)

    return f


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

a = ListNode(7000)
b = ListNode(200)
c = ListNode(300)
d = ListNode(700)
a.next = b
b.next = c
c.next = d

e = ListNode(7000)
f = ListNode(600)
g = ListNode(700)
h = ListNode(800)
e.next = f
f.next = g
g.next = h


ll = addTwoHugeNumbers(a, e)

print_ll(ll)
