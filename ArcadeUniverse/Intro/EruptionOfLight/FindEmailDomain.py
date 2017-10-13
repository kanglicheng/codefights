def findEmailDomain(address):
    index = 0

    for j in range(len(address) - 1, -1, -1):
        index -= 1

        if address[j] == "@":
            break

    return address[index + 1:]
