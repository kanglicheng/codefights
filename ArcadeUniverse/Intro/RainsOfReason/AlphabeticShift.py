def alphabeticShift(inputString):
    a = ord("a")
    s = ""

    for l in inputString:
        s += chr((((ord(l) + 1 - a)) % 26) + a)

    return s
