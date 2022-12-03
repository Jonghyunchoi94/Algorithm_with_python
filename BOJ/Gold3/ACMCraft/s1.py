import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(tree, status, node):
    if status[node] != -1:
        return status[node]
    if not tree[node]:
        status[node] = time[node]
        return time[node]
    t = -987654321
    for i in tree[node]:
        t = max(t, dfs(tree, status, i))

    status[node] = time[node] + t
    return time[node] + t

for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    time = [0] + time
    status = [-1] * (K + 1)
    purpose = [[] for _ in range(K + 1)]
    for _ in range(K):
        i, j = map(int, input().split())
        purpose[j].append(i)
    W = int(input())

    answer = dfs(purpose, status, W)
    print(answer)
