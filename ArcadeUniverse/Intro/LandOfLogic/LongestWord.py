def longestWord(text):
    found = re.findall("[a-zA-Z]+", text)

    word = ""

    for f in found:
        if len(f) > len(word):
            word = f

    return word
