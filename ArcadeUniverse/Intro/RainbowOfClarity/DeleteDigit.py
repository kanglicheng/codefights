def deleteDigit(n):
    nums = []
    num_str = str(n)

    for j in range(len(num_str)):
        nums.append(int(num_str[:j] + num_str[j + 1:]))

    return max(nums)
