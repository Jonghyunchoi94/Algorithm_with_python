import sys
sys.stdin = open('input.txt')

T = int(input())

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

hole = {
    1 : [0, 1, 2, 3],
    2 : [0, 2],
    3 : [1, 3],
    4 : [0, 1],
    5 : [1, 2],
    6 : [2, 3],
    7 : [0, 3],
}

direction = {
    0 : 2,
    1 : 3,
    2 : 0,
    3 : 1,
}

def dfs(r, c, time):
    if time == L:
        return

    for k in range(4):
        if k in hole[road[r][c]]:
            next_r = r + dr[k]
            next_c = c + dc[k]
            if 0 <= next_r < N and 0 <= next_c < M and visited[next_r][next_c] == 0 and road[next_r][next_c] and (direction[k] in hole[road[next_r][next_c]]):
                record.add((next_r, next_c))
                visited[next_r][next_c] = 1
                dfs(next_r, next_c, time + 1)
                visited[next_r][next_c] = 0
    return





for case in range(T):
    N, M, R, C, L = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    record = {(R, C)}
    dfs(R, C, 1)
    print('#{} {}'.format(case + 1, len(record)))