def getCommit(commit):
    return "".join(c for c in commit if c not in "0?+!")
