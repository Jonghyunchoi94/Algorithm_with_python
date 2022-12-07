import sys
sys.setrecursionlimit(10 ** 9)
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dfs(r, c, graph):

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]) and graph[nr][nc] == 1 and (nr, nc) not in visited:
            visited.add((nr, nc))
            dfs(nr, nc, graph)

    return

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]
    res = 0
    visited = set()
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and (i, j) not in visited:
                dfs(i, j, graph)
                res += 1
    print(res)

