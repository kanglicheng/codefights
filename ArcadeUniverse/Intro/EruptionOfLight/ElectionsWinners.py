def electionsWinners(votes, k):
    mx = max(votes)
    mxs = 0
    wins = 0

    for v in votes:
        if v + k > mx:
            wins += 1

        if v == mx:
            mxs += 1

    if wins == 0 and mxs == 1:
        return wins + 1

    return wins
