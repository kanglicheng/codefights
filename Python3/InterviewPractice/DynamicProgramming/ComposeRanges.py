def composeRanges(nums):
    print()

    if len(nums) == 0:
        return nums

    if len(nums) == 1:
        return [str(nums[0])]

    r = []
    t = [nums[0]]


    for i in range(1, len(nums)):
        if nums[i - 1] + 1 < nums[i]:
            if len(t) == 1:
                r.append(str(t[0]))
            else:
                r.append("{}->{}".format(t[0], t[len(t) - 1]))

            t = []

        t.append(nums[i])

    if len(t) == 1:
        r.append(str(t[0]))
    else:
        r.append("{}->{}".format(t[0], t[len(t) - 1]))

    return r


nums = [-1, 0, 1, 2, 6, 7, 9]
nums1 = [1, 2, 3]
nums2 = [1, 5]

print(composeRanges(nums))
print(composeRanges(nums1))
print(composeRanges(nums2))
