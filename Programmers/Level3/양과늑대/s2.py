info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

import heapq

def pobe(info, tree, node):
    pos = 2
    for n in tree[node]:
        if info[n] == 0:
            pos -= 1
    return pos

def solution(info, edges):
    answer = 0

    tree = [[] for _ in range(len(info))]

    for s, e in edges:
        tree[s].append(e)

    print(info)
    print(tree)

    pq = [(-1, pobe(info, tree, 0), 0)]
    val = 0
    while pq:
        print(pq)
        print(answer)
        animal, possibility, node = heapq.heappop(pq)

        if len(tree[node]) == 0 and info[node] == 1:
            continue
        elif len(tree[node]) == 0 and info[node] == 0:
            answer += 1
            val += 1
            continue
        elif info[node] == 1 and val <= 1:
            continue
        elif info[node] == 1:
            val -= 1
        elif info[node] == 0:
            answer += 1
            val += 1

        for nxt in tree[node]:
            if info[nxt] == 1:
                heapq.heappush(pq, (1, pobe(info, tree, nxt), nxt))
            elif info[nxt] == 0:
                heapq.heappush(pq, (-1, pobe(info, tree, nxt), nxt))

    return answer


print(solution(info, edges))

