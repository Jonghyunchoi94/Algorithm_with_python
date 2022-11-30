n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

import queue

INF = 987654321

def dijkstra(n, graph, src, dst, traps):
    pq = queue.PriorityQueue()
    visited = [[False] for _ in range(1<<len(traps))]

    return

def solution(n, start, end, roads, traps):
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    for u, v, w in roads:
        if w < graph[u][v]:
            graph[u][v] = w

    return dijkstra(n, graph, start, end, traps)

print(solution(n, start, end, roads, traps))