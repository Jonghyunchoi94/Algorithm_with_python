import sys
sys.stdin = open("input.txt")

N = int(input())
parent = list(map(int, input().split()))
R = int(input())

answer = 0
tree = [[] for _ in range(N)]

for i in range(len(parent)):
    if parent[i] == -1:
        start = i
        continue
    tree[parent[i]].append(i)

def dfs(Node):
    global answer
    if Node == R:
        return
    if (not tree[Node]) or (tree[Node] == [R]):
        answer += 1
        return

    for i in tree[Node]:
        dfs(i)

    return

dfs(start)

print(answer)