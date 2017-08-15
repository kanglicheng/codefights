# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    p = None
    c = l

    while c != None:
        if c.value == k:
            if p == None:
                l = c.next
                c = c.next
                continue

            p.next = c.next
            c = c.next
            continue

        p = c
        c = c.next

    return l
