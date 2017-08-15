#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def isTreeSymmetric(t):
    if t == None:
        return True

    lvl = [t]
    n_lvl = []

    while lvl:
        e = True

        for m in lvl:
            if m:
                n_lvl.append(m.left)
                n_lvl.append(m.right)

                if m.left:
                    print(m.left.value, end = " ")
                else:
                    print("None", end = " ")
                if m.right:
                    print(m.right.value, end = " ")
                else:
                    print("None", end = " ")
        print()

        for n in range(len(n_lvl) // 2):
            if n_lvl[n] is None and n_lvl[-1 - n] is None:
                continue
            if n_lvl[n] and n_lvl[-1 - n]:
                if n_lvl[n].value == n_lvl[-1 - n].value:
                    continue
            return False


        lvl = n_lvl
        n_lvl = []

        print()
    return True

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

a = Tree(1)
b = Tree(2)
c = Tree(2)
d = Tree(3)
e = Tree(4)
f = Tree(3)
g = Tree(4)

a.left = b
a.right = c
b.left = None
b.right = e
c.left = g
c.right = None

print(isTreeSymmetric(a))
