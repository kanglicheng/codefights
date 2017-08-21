def isTestSolvable(ids, k):
    digitSum = lambda questionId : sum(int(s) for s in str(questionId))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
