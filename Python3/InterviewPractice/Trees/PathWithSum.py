#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#

def hasPathWithGivenSum(t, s):
    if t is None:
        if s is 0:
            return True
        return False

    d = 0
    v = [(t, t.value)]

    while v:
        while t:
            d += t.value

            if t.left == None and t.right == None and d == s:
                return True

            if t.right:
                v.append((t.right, d))

            t = t.left

        t = v.pop()
        d = t[1]
        t = t[0]

    return False

##################
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

a = Tree(4)
b = Tree(1)
c = Tree(3)
d = Tree(-2)
e = Tree(1)
f = Tree(2)
g = Tree(3)
h = Tree(-2)
i = Tree(-3)

a.left = b
a.right = c
b.left = d
d.right = g
c.left = e
c.right = f
f.left = h
f.right = i

print(hasPathWithGivenSum(a, 7))
