import sys
sys.stdin = open('input.txt')

C = int(sys.stdin.readline())

for _ in range(C):
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        graph.append(s)

    print(graph)