# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 and l2 is None:
        return
    if l2 and l1 is None:
        return l2

    c1 = l1
    c2 = l2

    print_ll(c1)
    print_ll(c2)

    if l1.value < l2.value:
        s = l1
    else:
        s = l2

    print("start:", s.value)

    while c1 and c2:
        print_ll(s)
        while c1.value < c2.value:
            if c1.next == None:
                break
            c1 = c1.next
        print("c1 is...", c1.value)

        while c2.value < c1.value:
            if c2.next == None:
                break
            c2 = c2.next
        print("c2 is...", c2.value)


        print("c1, c2:", c1.value, c2.value)
        if c1.value < c2.value:
            print("c1 point to...:", c2.value)
            l1 = c1
            c1 = c1.next
            l1.next = c2
        else:
            print("c2 point to...:", c1.value)
            l2 = c2
            c2 = c2.next
            l2.next = c1


    return s


def mergeTwoLinkedLists(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 and l2 is None:
        return
    if l2 and l1 is None:
        return l2

    if l1.value < l2.value:
        s = l1
    else:
        s = l2

    c = s
    t = s

    print("start:", s.value)

    while l1 and l2:
        if l1.value < l2.value:
            c = l1
            l1 = l1.next
        else:
            c = l2
            l2 = l2.next

        t.next = c
        t = t.next

    if l1:
        t.next = l1
    if l2:
        t.next = l2

    return s

def print_ll(ll):
    while ll:
        print(ll.value, end = " ")
        ll = ll.next
    print()

class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

"""
a = ListNode(1)
b = ListNode(3)
c = ListNode(5)
d = ListNode(7)
a.next = b
b.next = c
c.next = d

e = ListNode(4)
f = ListNode(5)
g = ListNode(7)
h = ListNode(9)
i = ListNode(11)
e.next = f
f.next = g
g.next = h
h.next = i

##########
"""

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
i = ListNode(9)
e.next = f
f.next = g
g.next = h
h.next = i

"""
a = ListNode(1)
b = ListNode(1)
c = ListNode(2)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

e = ListNode(0)
f = ListNode(3)
g = ListNode(5)
e.next = f
f.next = g
"""

print_ll(mergeTwoLinkedLists(a, e))
