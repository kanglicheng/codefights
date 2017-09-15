def isIPv4Address(inputString):
    addy = inputString.split(".")

    if len(addy) != 4:
        return False

    for d in addy:
        if d is "":
            return False

        for n in d:
            if n < "0" or n > "9":
                return False

        if int(d) > 255 or int(d) < 0:
            return False

    return True
