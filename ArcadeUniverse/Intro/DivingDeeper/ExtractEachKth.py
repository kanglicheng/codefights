def extractEachKth(inputArray, k):
    return [inputArray[j] for j in range(len(inputArray)) if j % k != k - 1]
