import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())

def prim():

    for _ in range(V):
        min_idx = -1
        min_val = 987654321

        for i in range(1, V + 1):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]
        visited[min_idx] = 1

        for i in range(1, V + 1):
            if not visited[i] and graph[min_idx][i] < key[i]:
                key[i] = graph[min_idx][i]
    return sum(key[1:])

graph = [[987654321] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    s, e, dist = map(int, input().split())
    graph[s][e] = dist
    graph[e][s] = dist

key = [987654321] * (V + 1)
key[1] = 0
visited = [0] * (V + 1)

print(prim())


