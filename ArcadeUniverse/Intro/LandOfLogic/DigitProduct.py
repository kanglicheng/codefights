def digitsProduct(product):
    if product == 1:
        return 1

    if product < 10:
        return int("1" + str(product))

    solutions = []
    digits = []

    for j in range(2, 10):
        if product % j == 0:
            digits.append([j, product // j])

    while digits:
        d = digits.pop()

        if d[1] < 10:
            solutions.append(int(str(d[0]) + str(d[1])))
            continue

        if d[1] > 9:
            for k in range(2, 10):
                if d[1] % k == 0:
                    digits.append([int(str(d[0]) + str(k)), d[1] // k])

    if not solutions:
        return -1

    return min(solutions)
