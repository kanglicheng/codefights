from itertools import permutations, islice

def kthPermutation(numbers, k):
    return list(islice(permutations(numbers), k - 1, k)).pop()
