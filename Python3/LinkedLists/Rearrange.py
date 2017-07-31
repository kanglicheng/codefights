# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    if n == 0:
        return l

    l = reverse_list(l)
    pv = l
    c = l

    while n > 0:
        if c.next == None:
            return reverse_list(l)
        pv = c
        c = c.next
        n -= 1

    pv.next = None

    l = reverse_list(l)
    c = reverse_list(c)

    pv = l

    while l.next:
        l = l.next

    l.next = c

    return pv
    

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

print_ll(rearrangeLastN(a, 4))
