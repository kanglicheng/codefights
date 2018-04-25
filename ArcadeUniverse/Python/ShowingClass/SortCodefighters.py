def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return list(map(str, res))

class CodeFighter(object):
    def __init__(self, name, _id, xp):
        self.name = name
        self._id = int(_id)
        self.xp = int(xp)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.xp != other.xp:
            return self.xp < other.xp

        return self._id > other._id
