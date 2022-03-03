import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

"""
18352. bfs로 최단거리를 찾아야 시간복잡도의 문제가 줄어든다.
input = sys.stdin.readline으로 한 줄씩 읽는 것도 메모리에 영향을 준다.
"""

N, M, K, X = map(int, input().split())

mapData = [[] for _ in range(N + 1)]
distance = [0] * (N + 1)
visited = [False] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    mapData[s].append(e)

def bfs(start):
    res = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in mapData[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    res.append(i)
    if len(res) == 0:
        print(-1)
    else:
        res.sort()

        for j in res:
            print(j)

bfs(X)