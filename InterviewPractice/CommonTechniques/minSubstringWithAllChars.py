def minSubstringWithAllChars(s, t):
    valid_strs = []

    start = 0
    finish = len(t)

    if s == "" or t == "":
        return ""

    while finish < len(s) + 1:
        print(s[start:finish])
        if contains_letters(s[start:finish], t):
            valid_strs.append(s[start:finish])
            start += 1
        else:
            finish += 1

    while start < finish:
        if contains_letters(s[start:finish], t):
            valid_strs.append(s[start:finish])

        start += 1

    min_valid = valid_strs[0]

    for valid in valid_strs:
        if len(valid) < len(min_valid):
            min_valid = valid

    return min_valid


def contains_letters(s, t):
    char_count = {}

    for char in t:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in s:
        if char in char_count:
            char_count[char] -= 1

    for key, val in char_count.items():
        if val > 0:
            return False

    return True
