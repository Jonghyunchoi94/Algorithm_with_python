import sys
sys.stdin = open('input.txt')

"""
dfs는 시간초과를 유발한다.
"""
N, M, K, X = map(int, input().split())

mapData = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    mapData[s].append(e)

visited = [987654321] * (N + 1)

def dfs(start, distance):
    if distance < K:
        if distance < visited[start]:
            visited[start] = distance

    if distance == K:
        if distance < visited[start]:
            visited[start] = distance
        return

    for i in range(len(mapData[start])):
        dfs(mapData[start][i], distance + 1)

dfs(X, 0)

Flag = True
for i in range(1, N + 1):
    if visited[i] == K:
        print(i)
        Flag = False

if Flag:
    print(-1)
