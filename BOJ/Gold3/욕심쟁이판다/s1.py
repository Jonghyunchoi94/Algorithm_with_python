import sys
sys.stdin = open('input.txt')

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt, res

    if cnt > res:
        res = cnt

    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < n and 0 <= next_y < n  \
                and data[next_x][next_y] > data[x][y] and (next_x, next_y) not in visited:
            visited.add((next_x, next_y))
            cnt += 1
            dfs(next_x, next_y)
            cnt -= 1
            visited.remove((next_x, next_y))

res = 0

for i in range(n):
    for j in range(n):
        visited = set()
        visited.add((i, j))
        cnt = 1
        dfs(i, j)

print(res)