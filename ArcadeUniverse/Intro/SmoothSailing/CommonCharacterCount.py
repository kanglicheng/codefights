def commonCharacterCount(s1, s2):
    one = [0] * 26
    two = [0] * 26
    cnt = 0

    for i in s1:
        one[ord(i) - ord("a")] += 1

    for j in s2:
        two[ord(j) - ord("a")] += 1

    for k in range(len(two)):
        cnt += min(one[k], two[k])

    return cnt
