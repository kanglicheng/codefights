def findLongestSubarrayBySum(s, arr):
    if arr is None or len(arr) < 1:
        return [-1]

    total = arr[0]
    valid_indices = []
    start = 0
    finish = 0

    (start,
     finish,
     total,
     valid_indices) = walk_up(
        start,
        finish,
        total,
        valid_indices,
        s,
        arr)

    (start,
     finish,
     total,
     valid_indices) = walk_down(
        start,
        finish,
        total,
        valid_indices,
        s,
        arr)

    if not valid_indices:
        return [-1]

    return longest_last_pair(valid_indices)


def walk_up(start, finish, total, valid_indices, s, arr):
    while finish < len(arr):
        if total == s:
            valid_indices.append([start, finish])

        if total <= s:
            if finish + 1 == len(arr):
                break

            finish += 1
            total += arr[finish]
        else:
            total -= arr[start]
            start += 1

    return start, finish, total, valid_indices


def walk_down(start, finish, total, valid_indices, s, arr):
    while start < finish:
        total -= arr[start]
        start += 1

        if total == s:
            valid_indices.append([start, finish])
            break

    return start, finish, total, valid_indices


def longest_last_pair(arr):
    length = 0
    longest = 0
    longest_pair = arr[0]

    for valid in arr:
        length = valid[1] - valid[0]
        if longest <= length:
            longest = max(longest, length)
            longest_pair = valid

    return [longest_pair[0] + 1, longest_pair[1] + 1]
