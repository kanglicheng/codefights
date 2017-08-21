def newStyleFormatting(s):
    strs = s.split("%%")

    for i in range(len(strs)):
        strs[i] = re.sub("%[a-z]", "{}", strs[i])

    strs = "%".join(strs)

    return strs
