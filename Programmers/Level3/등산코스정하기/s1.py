n = 6
paths = [
    [1, 2, 3], [2, 3, 5], [2, 4, 2],
    [2, 5, 4], [3, 4, 4], [4, 5, 3],
    [4, 6, 1], [5, 6, 1]
]
gates = [1, 3]
summits = [5]

import heapq

def solution(n, paths, gates, summits):
    summits = set(summits)

    conn = [[] for _ in range(n + 1)]

    for i, j, w in paths:
        conn[i].append((j, w))
        conn[j].append((i, w))
    # print(conn)

    pq = [(0, gate) for gate in gates]
    MAX = 10000001
    min_dis = [MAX for _ in range(n + 1)]

    while pq:
        # print(pq)
        # print(min_dis)
        intensity, node = heapq.heappop(pq)
        if min_dis[node] <= intensity:
            continue
        min_dis[node] = intensity
        if node in summits:
            continue
        for nxt, nxt_w in conn[node]:
            nxt_w = max(intensity, nxt_w)
            if min_dis[nxt] <= nxt_w:
                continue
            heapq.heappush(pq, (nxt_w, nxt))

    answer = [0, MAX]

    for summit in summits:
        if min_dis[summit] < answer[1]:
            answer[0], answer[1] = summit, min_dis[summit]
        elif min_dis[summit] == answer[1] and summit < answer[0]:
            answer[0] = summit

    return answer

print(solution(n, paths, gates, summits))