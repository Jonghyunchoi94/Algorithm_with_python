import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())

dr = [0,0,1,-1]
dc = [1,-1,0,0]



for case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = data[:]
    ans = 987654321
    q = deque()
    print(data)
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                q.append([i,j])
                while q:
                    r, c = q.popleft()
                    if r == 0 or c = 0:


