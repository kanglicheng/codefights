def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for j in range(len(inputArray)):
        if inputArray[j] == elemToReplace:
            inputArray[j] = substitutionElem

    return inputArray
