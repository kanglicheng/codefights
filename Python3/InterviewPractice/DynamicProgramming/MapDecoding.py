def mapDecoding(message):
    if len(message) == 0:
        return 0

    if message[0] == "0":
        return 0

    if len(message) == 1:
        return 1

    i = 1
    m = 1
    r = range(1, 27)

    while i < len(message):
        if int(message[i - 1] + message[i]) < 27:
            m += 1

        i += 1
    return m

################################################
def mapDecoding(message):
    if len(message) == 0:
        return 0

    if message[0] == "0":
        return 0

    if len(message) == 1:
        return 1

    i = 1
    m = 1
    r = range(1, 27)

    while i < len(message):
        if message[i - 1] == "0":
            m += 1
        elif int(message[i - 1] + message[i]) < 27:
            m += 1
        elif message[i] == "0":
            return 0

        if message[i - 1] + message[i] == "00":
            return 0

        i += 1
    return m


###########################################


print(mapDecoding(""))
print(mapDecoding("1"))
print(mapDecoding("123"))
print(mapDecoding("301"))
print(mapDecoding("10122110"))
