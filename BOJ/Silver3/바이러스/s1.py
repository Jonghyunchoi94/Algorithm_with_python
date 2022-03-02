import sys
sys.stdin = open('input.txt')

Computer = int(input())
Line = int(input())

s = [[] for _ in range(Computer + 1)]

for _ in range(Line):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

visited = set()
visited.add(1)
def dfs(n):
    for i in range(len(s[n])):
        if s[n][i] not in visited:
            visited.add(s[n][i])
            dfs(s[n][i])

dfs(1)
print(len(visited) - 1)