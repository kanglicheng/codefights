def sumInRange(nums, queries):
    s = 0
    p = [0] * len(nums)

    p[0] = nums[0]
    p.insert(0, 0)

    print(p)

    for i in range(1, len(p)):
        p[i] = p[i - 1] + nums[i - 1]

    for q in queries:
        s += (p[q[1] + 1] - p[q[0]])

    return s % (10 ** 9 + 7)

# problem specified to modulo 10^9 + 7

n = [3, 0, -2, 6, -3, 2]
q = [[0, 2], [2, 5], [0, 5]]

p = [-1000]
l = [[0,0]]

print(sumInRange(n, q))
print(sumInRange(p, l))
