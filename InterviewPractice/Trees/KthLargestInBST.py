#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def kthLargestInBST(t, k):
    s = [t]
    f = []
    c = 1

    while s:
        while t:
            t = t.left
            s.append(t)

        m = s.pop()

        if m:
            f.append(m.value)

            if m.right:
                m = m.right
                s.append(m)

            c += 1
