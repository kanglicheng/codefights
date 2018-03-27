def sumInRange(nums, queries):
    s = 0
    p = [0] * len(nums)

    p[0] = nums[0]
    p.insert(0, 0)

    for i in range(1, len(p)):
        p[i] = p[i - 1] + nums[i - 1]

    for q in queries:
        s += (p[q[1] + 1] - p[q[0]])

    return s % (10 ** 9 + 7)
