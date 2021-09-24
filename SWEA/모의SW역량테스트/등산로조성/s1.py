import sys
sys.stdin = open('input.txt')

T = int(input())

def find_max(data):
    max_val = data[0][0]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > max_val:
                max_val = data[i][j]
    return max_val


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(i, j, road, arrange):
    visited[i][j] = 1
    global length
    if road > length:
        length = road


    for c in range(4):
        x = i + dx[c]
        y = j + dy[c]
        if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
            if data[i][j] > data[x][y]:
                dfs(x, y, road + 1, arrange)

            elif arrange and data[i][j] > data[x][y] - K:
                tmp = data[x][y]
                data[x][y] = data[i][j] - 1
                dfs(x, y, road + 1, False)
                data[x][y] = tmp

    visited[i][j] = 0

for case in range(T):
    N, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    length = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == find_max(data):
                dfs(i, j, 1, True)

    print('#{} {}'.format(case + 1, length))