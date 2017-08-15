#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def largestValuesInTreeRows(t):
    if t is None:
        return []

    lvl = [t]
    n_lvl = []

    t = []
    f = []

    for i in range(4):
        for m in lvl:
            t.append(m.value)

            if m.left:
                n_lvl.append(m.left)
            if m.right:
                n_lvl.append(m.right)

        if t:
            f.append(max(t))

        lvl = n_lvl
        n_lvl = []
        t = []

    return f


class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

a = Tree(1)
b = Tree(2)
c = Tree(4)
d = Tree(3)
e = Tree(5)

a.left = b
a.right = c
b.right = d
c.left = e

print(largestValuesInTreeRows(a))
