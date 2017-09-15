def arrayChange(inputArray):
    cnt = 0

    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            dx = inputArray[i] - inputArray[i + 1] + 1
            inputArray[i + 1] += dx
            cnt += dx

    return cnt
