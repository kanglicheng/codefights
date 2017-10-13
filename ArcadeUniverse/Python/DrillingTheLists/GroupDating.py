def groupDating(male, female):
    return [[male[j] for j in range(len(male)) if male[j] != female[j]], [female[k] for k in range(len(female)) if male[k] != female[k]]]
