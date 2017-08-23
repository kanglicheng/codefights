def adjacentElementsProduct(inputArray):
    if inputArray is None or len(inputArray) == 0:
        return None

    if len(inputArray) == 1:
        return inputArray[0]

    m = inputArray[0] * inputArray[1]

    for a in range(1, len(inputArray)):
        if inputArray[a - 1] * inputArray[a] > m:
            m = inputArray[a - 1] * inputArray[a]

    return m
    
