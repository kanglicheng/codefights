def isBeautifulString(inputString):
    freq = [0 for i in range(26)]

    for j in inputString:
        freq[ord(j) - ord("a")] += 1

    for k in range(len(freq) - 1):
        if freq[k] < freq[k + 1]:
            return False

    return True
