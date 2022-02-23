def solution(strings, n):
    res = sorted(strings)
    res = sorted(res, key=lambda x: x[n])
    return res