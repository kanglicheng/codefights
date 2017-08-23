def checkPalindrome(inputString):
    a = 0
    b = len(inputString) - 1

    while a < b:
        if inputString[a] != inputString[b]:
            return False

        a += 1
        b -= 1

    return True
