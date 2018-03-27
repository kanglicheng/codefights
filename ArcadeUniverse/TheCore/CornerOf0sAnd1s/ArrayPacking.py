def arrayPacking(nums):
    bin_str = ""
    for num in nums:
        bin_str = '{:08b}'.format(num) + bin_str

    return (int("".join(bin_str), 2))
