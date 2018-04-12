def possibleSums(coins, quantity):
    totals = {}

    for index, coin in enumerate(coins):
        run = range(coin, quantity[index] * coin + 1, coin)
        keys = list(totals.keys())

        for step in run:
            totals[step] = True

            for key in keys:
                totals[step + key] = True

    return len(totals)
