import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt")

N = int(input())

tree = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent = [0] * (N + 1)
parent[1] = 1

for _ in range(N - 1):
    S, E = map(int, input().split())
    tree[S].append(E)
    tree[E].append(S)


def dfs(Node):
    if visited[Node]:
        return
    visited[Node] = True

    for i in tree[Node]:
        if visited[i]:
            continue
        parent[i] = Node
        dfs(i)

dfs(1)

for i in range(2, N + 1):
    print(parent[i])