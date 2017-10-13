def sumUpNumbers(inputString):
    found = re.findall("[0-9]+", inputString)

    for j in range(len(found)):
        found[j] = int(found[j])

    return sum(found)
