def boxBlur(image):
    h = len(image)
    w = len(image[0])

    box_blur = []

    total = 0
    color = 0

    for j in range(1, h - 1):
        lvl = []
        for k in range(1, w - 1):
            total = (image[j - 1][k - 1]
                + image[j - 1][k]
                + image[j - 1][k + 1]
                + image[j][k - 1]
                + image[j][k]
                + image[j][k + 1]
                + image[j + 1][k - 1]
                + image[j + 1][k]
                + image[j + 1][k + 1])

            color = total // 9
            lvl.append(color)

        box_blur.append(lvl)

    return box_blur
