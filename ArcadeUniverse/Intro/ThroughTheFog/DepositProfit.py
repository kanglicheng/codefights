def depositProfit(deposit, rate, threshold):

    years = 0

    while deposit < threshold:
        deposit = deposit + deposit * (rate * 0.01)
        years += 1

    return years
