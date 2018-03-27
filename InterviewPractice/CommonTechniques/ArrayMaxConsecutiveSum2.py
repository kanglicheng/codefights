def arrayMaxConsecutiveSum2(inputArray):
    if inputArray == None or len(inputArray) < 1:
        return None

    if len(inputArray) == 1:
        return inputArray[0]

    pv = inputArray[0]
    mx = inputArray[0]

    for m in range(1, len(inputArray)):
        pv = max(inputArray[m], inputArray[m] + pv)
        mx = max(mx, pv)

    return mx
