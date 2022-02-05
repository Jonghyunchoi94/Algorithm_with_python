import sys
sys.stdin = open("input.txt")

N, M = map(int, input().split())

city = []
minimum_cost = [987654321] * (N + 1)


for _ in range(M):
    A, B, C = map(int, input().split())
    city.append((A, B, C))

minimum_cost[1] = 0
Flag = False

for i in range(N):
    for j in range(M):
        node = city[j][0]
        next_node = city[j][1]
        cost = city[j][2]

        if minimum_cost[node] != 987654321 and minimum_cost[next_node] > minimum_cost[node] + cost:
            minimum_cost[next_node] = minimum_cost[node] + cost
            if i == N - 1:
                Flag = True
if Flag:
    print(-1)
else:
    for i in range(2, N + 1):
        if minimum_cost[i] != 987654321:
            print(minimum_cost[i])
        else:
            print(-1)
