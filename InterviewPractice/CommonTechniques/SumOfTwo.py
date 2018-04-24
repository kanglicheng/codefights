def sumOfTwo(a, b, v):
    hashy = {}

    for number in a:
        if v - number not in hashy:
            hashy[v - number] = True

    for number in b:
        if number in hashy:
            return hashy[number]

    return False
