def checkPassword(attempts, password):
    def check():
        while True:
            val = yield
            yield password == val

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
