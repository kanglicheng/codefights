def lateRide(n):
    f = n // 60
    l = n % 60

    return f // 10 + f % 10 + l // 10 + l % 10
