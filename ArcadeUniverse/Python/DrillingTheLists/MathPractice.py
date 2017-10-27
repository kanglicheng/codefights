from functools import reduce

def mathPractice(numbers):
    return reduce(lambda x, y: (x + numbers[y]) * numbers[y + 1] if y + 1 < len(numbers) else x + numbers[y], [i for i in range(1, len(numbers), 2)], numbers[0])
