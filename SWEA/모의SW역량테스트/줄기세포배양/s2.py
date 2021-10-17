import sys
sys.stdin = open('input3.txt')

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]


T = int(input())

for case in range(T):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    original = []
    visited = {}
    time_limit = {}
    change_visit = {}
    for i in range(N):
        for j in range(M):
            if data[i][j]:
                q.append((i, j, data[i][j], 0))
                original.append((i, j))
                visited[(i, j)] = data[i][j]
                time_limit[(i, j)] = 0
                change_visit[(i, j)] = data[i][j] - K
    while q:
        r, c, status, time = q.popleft()
        if time >= K:
            continue
        if status > 0:
            q.append((r, c, status - 1, time + 1))
            continue

        for k in range(4):
            next_r = r + dr[k]
            next_c = c + dc[k]
            if (next_r, next_c) not in visited:
                visited[(next_r, next_c)] = visited[(r, c)]
                time_limit[(next_r, next_c)] = time + 1
                change_visit[(next_r, next_c)] = visited[(r, c)] - K + time + 1
                q.append((next_r, next_c, visited[(r, c)], time + 1))
            elif visited[(r, c)] > visited[(next_r, next_c)] and (next_r, next_c) not in original and time + 1 <= time_limit[(next_r, next_c)]:
                visited[(next_r, next_c)] = visited[(r, c)]
                time_limit[(next_r, next_c)] = time + 1
                change_visit[(next_r, next_c)] = visited[(r, c)] - K + time + 1
                q.append((next_r, next_c, visited[(r, c)], time + 1))

    print(visited)
    print(len(visited))
    print(time_limit)
    print(change_visit)
    cnt = 0
    for k, v in change_visit.items():
        if v >= - time_limit[k]:
            cnt += 1

    print(cnt)



