import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())


def dfs(n, k, cnt):
    if cnt == 1:
        return

    return

for _ in range(T):
    N = int(sys.stdin.readline())
    l = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        l.append((x, y))
