def isMAC48Address(inputString):
    if re.search("^([0-9A-F]{2}[-]){5}[0-9A-F]{2}$", inputString):
        return True

    return False
