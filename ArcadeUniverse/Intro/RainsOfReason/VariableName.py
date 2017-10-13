def variableName(name):

    if name[0] >= "0" and name[0] <= "9":
        return False

    for l in name:
        if l == "_":
            continue

        if l >= "0" and l <= "9":
            continue

        if l >= "a" and l <= "z":
            continue

        if l >= "A" and l <= "Z":
            continue

        return False

    return True
