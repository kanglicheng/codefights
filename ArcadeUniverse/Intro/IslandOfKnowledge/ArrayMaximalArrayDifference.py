def arrayMaximalAdjacentDifference(inputArray):
    mx = 0

    for j in range(len(inputArray) - 1):
        mx = max(mx, abs(inputArray[j + 1] - inputArray[j]))

    return mx
