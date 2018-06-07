class Team(object):
    def __init__(self, names):
        self.names = names

    def __bool__(self):
        firsts = {}
        lasts = {}

        for name in self.names:
            first = name[0].lower()
            last = name[-1].lower()

            if first in firsts:
                firsts[first] += 1
            else:
                firsts[first] = 1
            if last in lasts:
                lasts[last] += 1
            else:
                lasts[last] = 1

        for letter, count in lasts.items():
            if letter in firsts:
                firsts[letter] = max(firsts[letter] - count, 0)

        return sum(firsts.values()) < 2


def isCoolTeam(team):
    return bool(Team(team))
