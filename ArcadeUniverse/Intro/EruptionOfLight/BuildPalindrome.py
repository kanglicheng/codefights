def buildPalindrome(st):
    plndrm = st[::-1]
    index = 0

    for j in range(len(plndrm)):
        if st[j:] == plndrm[:len(plndrm) - j]:
            return st[:j] + plndrm
