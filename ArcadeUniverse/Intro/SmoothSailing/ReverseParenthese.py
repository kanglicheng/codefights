def reverseParentheses(s):
    rvrsd = True

    while rvrsd:
        il = 0
        ir = 0

        for i in range(len(s)):
            if s[i] == "(":
                il = i

            if s[i] == ")":
                ir = i
                break

        if ir == 0:
            break

        s = s[:il] + s[ir - 1:il: -1] + s[ir + 1:]

    return s
            
