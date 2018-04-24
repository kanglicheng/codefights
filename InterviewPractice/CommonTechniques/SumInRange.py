def sumInRange(nums, queries):
    sum_of_pairs = 0
    pair_sums = [0 for space in range(len(nums) + 1)]

    for j in range(1, len(pair_sums)):
        pair_sums[j] = pair_sums[j - 1] + nums[j - 1]

    for query in queries:
        sum_of_pairs += pair_sums[query[1] + 1] - pair_sums[query[0]]

    return sum_of_pairs % (10 ** 9 + 7)
