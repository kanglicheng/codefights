def productExceptSelf(nums, m):
    prev = 1
    gross = 0

    for num in nums:
        gross = (gross * num + prev) % m
        prev = (prev * num) % m

    return gross


def productExceptSelf(nums, m):
    preProd = [1 for x in range(len(nums))]
    sufProd = [1 for x in range(len(nums))]

    for i in range(1, len(nums)):
        preProd[i] = (preProd[i - 1] * nums[i - 1]) % m

    for j in range(len(nums) - 1, 0, -1):
        sufProd[j - 1] = (sufProd[j] * nums[j]) % m

    total = 0

    for i in range(len(nums)):
        total += (preProd[i] * sufProd[i]) % m

    return total % m
