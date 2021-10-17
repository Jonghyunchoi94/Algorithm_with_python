import sys
sys.stdin = open('input3.txt')

from collections import deque
from copy import deepcopy

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


T = int(input())

for case in range(T):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    copy_data = deepcopy(data)

    q = deque()
    visited = {}
    change_visit = {}
    time_limit = {}
    original = []
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                q.append((i, j, 0))
                time_limit[(i, j)] = 0
                original.append((i, j))
                visited[(i, j)] = data[i][j]
                change_visit[(i, j)] = data[i][j]

    while q:
        r, c, time = q.popleft()
        if (r, c, time) in q:
            continue
        if time > K:
            continue

        for k in range(4):
            next_r = r + dr[k]
            next_c = c + dc[k]
            if (next_r, next_c) not in visited:
                visited[(next_r, next_c)] = visited[(r, c)]
                time_limit[(next_r, next_c)] = time + 1
                change_visit[(next_r, next_c)] = visited[(r, c)]
                q.append((next_r, next_c, time + 1))
            elif visited[(r, c)] > change_visit[(next_r, next_c)] and (next_r, next_c) not in original and time + 1 <= time_limit[(next_r, next_c)]:
                visited[(next_r, next_c)] = visited[(r, c)]
                change_visit[(next_r, next_c)] = visited[(r, c)]
                time_limit[(next_r, next_c)] = time + 1
                q.append((next_r, next_c, time + 1))
    cnt = 0
    for k, v in change_visit.items():
        if (v * 2) - time_limit[k] > 0:
            cnt += 1

    print(cnt)

