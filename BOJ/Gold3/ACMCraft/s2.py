import sys
sys.stdin = open('input.txt')


from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    time = [0] + time
    degree = [0] * (N + 1)
    status = [0] * (N + 1)
    purpose = [[] for _ in range(N + 1)]
    for _ in range(K):
        i, j = map(int, input().split())
        purpose[i].append(j)
        degree[j] += 1
    W = int(input())
    q = deque()

    for k in range(1, N + 1):
        if degree[k] == 0:
            q.append(k)
            status[k] = time[k]

    while q:
        now = q.popleft()

        for t in purpose[now]:
            degree[t] -= 1
            status[t] = max(status[t], status[now] + time[t])
            if degree[t] == 0:
                q.append(t)
    print(status[W])
