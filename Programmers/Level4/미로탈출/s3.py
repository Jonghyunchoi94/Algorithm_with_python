n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]

from collections import defaultdict
import heapq

def changeroad(road, node):
    answer = [[] for _ in range(len(road) + 1)]
    for i in range(1, len(road)):
        for j, w in road[i]:
            if i == node:
                answer[j].append((i, w))
            elif j != node:
                answer[i].append((j, w))
            else:
                answer[j].append((i, w))
    return answer


def solution(n, start, end, roads, traps):

    board = [[] for _ in range(n + 1)]

    setroad = defaultdict(int)

    for i, j, w in roads:
        if (i, j) in setroad:
            setroad[(i, j)] = min(setroad[(i, j)], w)
        else:
            setroad[(i, j)] = w

    for a, b in setroad:
        board[a].append((b, setroad[(a, b)]))

    Flag = [[0] * len(traps) for _ in range(n + 1)]

    pq = [(0, start, board, Flag)]

    distance = [987654321 for _ in range(n + 1)]
    visited = []

    while pq:
        r, node, road, sign = heapq.heappop(pq)
        if node in traps:
            if sign[node][traps.index(node)] == 0:
                sign[node][traps.index(node)] = 1
            else:
                sign[node][traps.index(node)] = 0
        if (node, sign[node]) in visited:
            continue
        visited.append((node, sign[node]))
        distance[node] = r
        if node == end:
            break

        for nxt, nxt_w in road[node]:
            nw = r + nxt_w

            if nxt in traps:
                nroad = changeroad(road, nxt)
                heapq.heappush(pq, (nw, nxt, nroad, sign))
            else:
                heapq.heappush(pq, (nw, nxt, road, sign))


    # print(distance)

    return distance[end]

print(solution(n, start, end, roads, traps))