def traverseTree(t):
    if t is None:
        return []

    lvl = [t]
    n_lvl = []

    p = []

    while lvl:
        for m in lvl:
            p.append(m.value)

            if m.left:
                n_lvl.append(m.left)
            if m.right:
                n_lvl.append(m.right)

        lvl = n_lvl
        n_lvl = []

    return p

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

print(traverseTree(a))
