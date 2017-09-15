def addBorder(picture):
    border = []

    for j in picture:
        border.append("*" + j + "*")

    border.insert(0, ("*" * len(border[0])))
    border.append("*" * len(border[0]))

    return border
