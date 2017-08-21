def wordPower(word):
    num = dict(zip([chr(c) for c in range(97, 123)], [i for i in range(1, 27)]))
    return sum([num[ch] for ch in word])
