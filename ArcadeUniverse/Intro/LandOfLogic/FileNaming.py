def fileNaming(names):
    hashy = {}
    order = []

    for name in names:
        if name not in order:
            hashy[name] = 1
            order.append(name)
        else:
            number = hashy[name]
            new_name = "{}({})".format(name, number)

            while new_name in hashy:
                number += 1
                new_name = "{}({})".format(name, number)

            hashy[new_name] = 1
            order.append(new_name)

    return order
