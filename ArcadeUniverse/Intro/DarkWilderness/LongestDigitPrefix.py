def longestDigitsPrefix(inputString):
    prefix = ""

    for j in inputString:
        if j < "0" or j > "9":
            break

        prefix += j

    return prefix
