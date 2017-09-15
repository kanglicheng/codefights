def avoidObstacles(inputArray):
    s = dict(zip(inputArray, [None] * len(inputArray)))
    mx = max(inputArray)

    jump = 1
    clear = False

    while not clear:
        index = 0
        jump += 1

        while index < mx:
            if index not in s:
                index += jump
            else:
                break

        if index > mx:
            clear = True

    return jump
