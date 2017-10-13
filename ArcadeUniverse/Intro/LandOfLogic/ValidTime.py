def validTime(time):
    hr = int(time[:2])
    mn = int(time[3:])

    if hr < 0 or hr > 23:
        return False

    if mn < 0 or mn > 59:
        return False

    return True
