def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return "".join(sorted(list(set(list(w1)) - set(list(w2)))))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
