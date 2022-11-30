n = 9
path = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
order = [[8,5],[6,7],[4,1]]

from collections import defaultdict
from collections import deque
def solution(n, path, order):
    answer = True

    road = [[] for _ in range(n)]
    visited = [False] * n

    for i, j in path:
        road[i].append(j)
        road[j].append(i)
    # print(road)

    parent = defaultdict(int)
    child = defaultdict(int)

    for p, c in order:
        parent[c] = p

    pq = deque([0])

    while pq:
        node = pq.popleft()

        if node in parent.keys() and not visited[parent[node]]:
            child[parent[node]] = node
            continue

        visited[node] = True

        for l in road[node]:
            if not visited[l]:
                pq.append(l)

        if node in child.keys():
            pq.append(child[node])

    if False in visited:
        return False

    return answer

print(solution(n, path, order))