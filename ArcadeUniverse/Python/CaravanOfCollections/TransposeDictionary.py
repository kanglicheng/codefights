def transposeDictionary(scriptByExtension):
    return sorted(list(d[::-1] for d in scriptByExtension.items()))
