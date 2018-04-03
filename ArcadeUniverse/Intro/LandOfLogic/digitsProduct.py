def digitsProduct(product):
    if product == 0:
        return 10

    for j in range(1, product ** 2 + 1):
        digits = str(j)

        result = 1
        for digit in digits:
            result *= int(digit)

        if result == product:
            return int(digits)

    return -1
