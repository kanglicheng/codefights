def containsCloseNums(nums, k):
    if len(nums) < 2:
        return False

    d = {}

    for n in range(len(nums)):
        if nums[n] in d and n - d[nums[n]] <= k:
            return True

        d[nums[n]] = n

    return False
