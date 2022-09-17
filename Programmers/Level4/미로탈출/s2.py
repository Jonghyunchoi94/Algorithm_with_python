n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

from copy import deepcopy
import heapq

def solution(n, start, end, roads, traps):
    answer = 0

    board = [[0] * (n + 1) for _ in range(n + 1)]

    for i, j, w in roads:
        board[i][j] = w
    print(board)

    pq = [(0, start)]
    distance = [987654321 for _ in range(n + 1)]

    while pq:
        print(pq)
        r, node = heapq.heappop(pq)

        distance[node] = r
        if node == end:
            break

        for nxt, nxt_w in board[node]:
            nw = r + nxt_w
            if nxt in traps:
                heapq.heappush(pq, (nw, nxt))
            else:
                heapq.heappush(pq, (nw, nxt))


    print(distance)

    return distance[end]

print(solution(n, start, end, roads, traps))