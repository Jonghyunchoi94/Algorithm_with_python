import sys
sys.stdin = open('input.txt')

# 땅에서 물로  ( 시간 초과 error )

from collections import deque

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in range(T):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    ans = 0
    q = deque()
    for r in range(N):
        for c in range(M):
            if data[r][c] == 'L':
                visited = [[0] * M for _ in range(N)]
                less_visited = [[0] * M for _ in range(N)]
                q.append([r, c])
                less_visited[r][c] = 1
                while q:
                    x, y = q.popleft()
                    if data[x][y] == 'W':
                        ans += visited[x][y]
                        q.clear()
                        break
                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < N and 0 <= next_y < M and less_visited[next_x][next_y] == 0:
                            less_visited[next_x][next_y] = 1
                            visited[next_x][next_y] = visited[x][y] + 1
                            q.append([next_x, next_y])
    print('#{} {}'.format(case + 1, ans))








