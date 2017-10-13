def growingPlant(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = 0

    while height <= desiredHeight:
        height += upSpeed

        if height >= desiredHeight:
            break

        height -= downSpeed
        days += 1

    return days
