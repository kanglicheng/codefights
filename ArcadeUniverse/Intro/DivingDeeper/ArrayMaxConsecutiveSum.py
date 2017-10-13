def arrayMaxConsecutiveSum(inputArray, k):
    f = 0
    l = k
    total = 0
    mx = 0

    for j in range(k):
        total += inputArray[j]

    mx = max(mx, total)

    for k in range(k, len(inputArray)):
        total += inputArray[l]
        total -= inputArray[f]
        mx = max(mx, total)

        l += 1
        f += 1

    return mx
