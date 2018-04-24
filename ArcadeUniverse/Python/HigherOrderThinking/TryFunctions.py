def tryFunctions(x, functions):
    return list(map(lambda func: eval(func)(x), functions))
