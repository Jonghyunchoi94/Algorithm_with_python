from functools import cmp_to_key

def compare(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]

def solution(N, stages):
    answer = []
    total = len(stages)
    users = [0 for _ in range(N + 1)]
    fails = []

    for s in stages:
        users[s - 1] += 1

    for i in range(N):
        if users[i] == 0:
            fails.append((i + 1, 0))
        else:
            fails.append((i + 1, users[i] / total))
            total -= users[i]

    for f in sorted(fails, key=cmp_to_key(compare)):
        answer.append(f[0])

    return answer