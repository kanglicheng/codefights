def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    you = [yourLeft, yourRight]
    friend = [friendsLeft, friendsRight]

    if sum(you) != sum(friend):
        return False

    if you[0] not in friend:
        return False

    if you[1] not in friend:
        return False

    return True
