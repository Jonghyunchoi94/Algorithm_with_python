n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

from copy import deepcopy
from collections import deque

def comp(weak, dist):
    w = deque(weak)
    nw = weak[0] + dist
    while w:
        if nw < w[0]:
            break
        w.popleft()

    return list(w)


def solution(n, weak, dist):
    answer = 987654321
    visited = [0] * len(dist)
    w = deepcopy(weak)
    l = len(weak)
    for k in range(len(weak)):
        w.append(n + weak[k])

    def dfs(weak, dist, d):
        nonlocal visited, answer
        if not weak:
            if len(d) < answer:
                answer = len(d)
            return

        for i in range(len(dist)):
            if visited[i] == 0:
                visited[i] = 1
                temp = comp(weak, dist[i])
                d.append(i)
                dfs(temp, dist, d)
                d.pop()
                visited[i] = 0

        return

    for i in range(len(weak)):
        visited = [0] * len(dist)
        dfs(w[i: i + l], dist, [])

    if answer == 987654321:
        return -1

    return answer


print(solution(n, weak, dist))

