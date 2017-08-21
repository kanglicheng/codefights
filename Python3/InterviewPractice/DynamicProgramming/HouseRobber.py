def houseRobber(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    t = [0, nums[0], nums[1]]

    for i in range(3, len(nums) + 1):
        n = max(t[0], t[1]) + nums[i - 1]
        t[0], t[1], t[2] = t[1], t[2], n

    return max(t[1], t[2])
