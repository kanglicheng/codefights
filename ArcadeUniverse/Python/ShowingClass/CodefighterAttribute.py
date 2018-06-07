class CodeFighter(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id

        self.xp = xp
        self.name = name

    def __dir__(self):
        return ['username', '_id', 'xp', 'name']

    def __getattr__(self, attribute):
        if attribute in dir(self):
            return self[attribute]
        else:
            return "{} attribute is not defined".format(attribute)


def codefighterAttribute(attribute):
    codefighter = CodeFighter("annymaster", "1234567", "1500", "anny")
    return getattr(codefighter, attribute)
