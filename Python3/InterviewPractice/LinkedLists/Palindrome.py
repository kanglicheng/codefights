# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def isListPalindrome(l):
    if l == None or l.next == None:
        return True

    s = l
    f = l

    # find odd or even
    while True:
        s = s.next
        f = f.next.next

        if f == None:
            break

        if f.next == None:
            s = s.next
            break

    # reverse second linked list
    p = None
    c = s
    n = None

    while c:
        n = c.next
        c.next = p
        p = c
        c = n

    # check if palindrome
    s = l
    c = p

    while c:
        if c.value != s.value:
            return False

        s = s.next
        c = c.next

    return True


class node(object):
    def __init__(self, x):
        self.value = x
        self.next = None

### testers
a = node(1)
b = node(2)
c = node(3)
d = node(2)
e = node(1)
a.next = b
b.next = c
c.next = d
d.next = e

f = node(1)
g = node(2)
h = node(3)
i = node(2)
f.next = g
g.next = h
h.next = i


# 1 -> 2 -> 3 -> 2 -> 1

print(isListPalindrome(a))
print(isListPalindrome(f))
