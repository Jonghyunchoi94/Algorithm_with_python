import sys
sys.stdin = open('input.txt')

# 물에서 땅으로 (최적화 완료 !! )

from collections import deque

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for case in range(T):
    N, M = map(int, input().split())
    # 매우 중요한 insight
    # list(input()) 으로 할 시 runtime error !
    # input() 으로 할 시 통과 !

    data = [input() for _ in range(N)]
    less_visited = [[987654321] * M for _ in range(N)]
    q = deque()
    for r in range(N):
        for c in range(M):
            if data[r][c] == 'W':
                q.append([r, c])
                less_visited[r][c] = 0
    # 연산량을 줄이기 위해 불필요한 계산 줄이는 방법 !!
    while q:
        x, y = q.popleft()
        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < N and 0 <= next_y < M and data[next_x][next_y] == 'L' and less_visited[next_x][next_y] == 987654321:
                less_visited[next_x][next_y] = less_visited[x][y] + 1
                q.append([next_x, next_y])
    res = 0
    for i in less_visited:
        for j in i:
            res += j
    print('#{} {}'.format(case + 1, res))
