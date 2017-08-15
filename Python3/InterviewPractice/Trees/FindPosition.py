def findProfession(level, pos):
    m = "Engineer"

    if level == 1:
        return m

    l = 1
    r = 2 ** (level - 1)
    c = r // 2

    while level != 1:
        print("l, c, r:", l, c, r)

        if pos <= c:
            r = c
            c = l + ((r - l) // 2)
            print("left...")

        if pos > c:
            l = c + 1
            c = l + ((r - l) // 2)
            print("right...")

            if m == "Doctor":
                m = "Engineer"
                continue

            m = "D"

        level -= 1
        print("m:", m)

    print("c:", c)
    print("m:", m)

    return m



#print(findProfession(1, 1))
#print(findProfession(2, 1))
print(findProfession(8, 100))
#print(findProfession(17, 5921))
#print(findProfession(4, 2))
#print(findProfession(20, 171971))
#print(findProfession(30, 163126329))
