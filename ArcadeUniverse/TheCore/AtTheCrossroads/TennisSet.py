def tennisSet(score1, score2):
    if score1 < score2:
        score2, score1 = score1, score2

    if score1 + score2 > 13:
        return False
    if score1 == 7 and score2 > 4:
        return True
    if score1 == 6 and score2 < 5:
        return True

    return False
