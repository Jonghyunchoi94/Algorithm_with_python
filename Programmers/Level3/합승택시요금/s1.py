n = 6
s = 4
a = 5
b = 6
fares = [
    [2,6,6], [6,3,7], [4,6,7],
    [6,5,11], [2,5,12], [5,3,20],
    [2,4,8], [4,3,9]
]

import heapq

def solution(n, s, a, b, fares):
    road = [[987654321] * (n + 1) for _ in range(n + 1)]

    for start, end, fare in fares:
        road[start][end] = fare
        road[end][start] = fare


    money = [[987654321] * (n + 1) for _ in range(n + 1)]

    pq = [(0, n, n) for n in range(1, n + 1)]

    while pq:
        cost, node, start = heapq.heappop(pq)
        if money[start][node] <= cost:
            continue
        money[start][node] = cost
        for i in range(1, n + 1):
            if i != node or road[node][i] != 987654321:
                heapq.heappush(pq, (cost + road[node][i], i, start))

    res = 987654321
    for i in range(1, n + 1):
        if res > money[s][i] + money[i][a] + money[i][b]:
            res = money[s][i] + money[i][a] + money[i][b]


    return res

print(solution(n, s, a, b, fares))

