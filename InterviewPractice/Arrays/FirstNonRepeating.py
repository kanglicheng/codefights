def firstNotRepeatingCharacter(s):
    chars = [0] * 26

    for c in s:
        chars[ord(c) - ord("a")] += 1

    for c in s:
        if chars[ord(c) - ord("a")] == 1:
            return c

    return "_"
