n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]


import heapq

def solution(n, start, end, roads, traps):
    answer = 0

    odd_board = [[] for _ in range(n + 1)]
    even_board = [[] for _ in range(n + 1)]

    for i, j, w in roads:
        odd_board[i].append((j, w))
        even_board[j].append((i, w))
    # print(odd_board)
    # print(even_board)

    pq = [(0, start, 0)]

    distance = [987654321 for _ in range(n + 1)]



    while pq:
        r, node, turn = heapq.heappop(pq)

        if distance[node] <= r:
            continue

        distance[node] = r

        if turn % 2:
            for nxt, nxt_w in even_board[node]:
                nw = r + nxt_w
                if distance[nxt] <= nw:
                    continue
                if nxt in traps:
                    heapq.heappush(pq, (nw, nxt, turn + 1))
                else:
                    heapq.heappush(pq, (nw, nxt, turn))
        else:
            for nxt, nxt_w in odd_board[node]:
                nw = r + nxt_w
                # if distance[nxt] <= nw:
                #     continue
                if nxt in traps:
                    heapq.heappush(pq, (nw, nxt, turn + 1))
                else:
                    heapq.heappush(pq, (nw, nxt, turn))

    print(distance)

    return distance[end]

print(solution(n, start, end, roads, traps))