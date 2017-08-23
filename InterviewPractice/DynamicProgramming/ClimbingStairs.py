def climbingStairs(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    stck = [1, 2]
    curr = 2

    while curr < n:
        total = stck[0] + stck[1]
        stck[0] = stck[1]
        stck[1] = total

        curr += 1

    return stck[1]
