"""
one node, any other node, at most two nodes
"""

def efficientRoadNetwork(n, roads):
    mp = {}
    ns = []

    if n == 1 and roads == []:
        return True

    for i in range(n):
        mp[i] = {}

    for r in roads:
        mp[r[0]][r[1]] = True
        mp[r[1]][r[0]] = True

    for i in range(n):
        ns = [False] * n

        for j in mp[i]:
            ns[j] = True

            for k in mp[j]:
                ns[k] = True

        if not all(ns):
            return False

    print(mp)
    return True
