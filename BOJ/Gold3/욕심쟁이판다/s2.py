import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)
n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):

    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for k in range(4):
        next_x = x + dx[k]
        next_y = y + dy[k]

        if 0 <= next_x < n and 0 <= next_y < n  \
                and data[next_x][next_y] > data[x][y]:
            dp[x][y] = max(dp[x][y], dfs(next_x, next_y) + 1)

    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))

print(ans)