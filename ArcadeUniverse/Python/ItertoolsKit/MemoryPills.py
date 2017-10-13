from itertools import chain, dropwhile

def memoryPills(pills):
    gen = chain(dropwhile(lambda x: len(x) % 2 != 0, pills), ["" for p in range(3)])
    next(gen)
    return [next(gen) for _ in range(3)]
