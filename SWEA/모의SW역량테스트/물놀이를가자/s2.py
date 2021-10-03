import sys
sys.stdin = open('input.txt')

# 물에서 땅으로 ( 제한 시간 초과 )

from collections import deque

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    less_visited = [[987654321] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if data[r][c] == 'W':
                visited = [[0] * M for _ in range(N)]
                q = deque()
                q.append([r, c])
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        next_x = x + dx[k]
                        next_y = y + dy[k]
                        if 0 <= next_x < N and 0 <= next_y < M and data[next_x][next_y] == 'L' and visited[next_x][next_y] == 0:
                            visited[next_x][next_y] = visited[x][y] + 1
                            if visited[next_x][next_y] < less_visited[next_x][next_y]:
                                less_visited[next_x][next_y] = visited[next_x][next_y]
                            q.append([next_x, next_y])
    res = 0
    for i in range(N):
        for j in range(M):
            if less_visited[i][j] != 987654321:
                res += less_visited[i][j]
    print('#{} {}'.format(case + 1, res))








