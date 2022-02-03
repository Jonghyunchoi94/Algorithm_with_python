import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 1

while True:
    N = int(input())
    if N == 0:
        break
    map_data = [list(map(int, input().split())) for _ in range(N)]
    cost_data = [[987654321] * N for _ in range(N)]
    cost_data[0][0] = map_data[0][0]

    q = deque([[0, 0]])

    while q:
        x, y = q.popleft()

        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]

            if 0 <= next_x < N and 0 <= next_y < N:
                if cost_data[next_x][next_y] > cost_data[x][y] + map_data[next_x][next_y]:
                    cost_data[next_x][next_y] = cost_data[x][y] + map_data[next_x][next_y]
                    q.append([next_x, next_y])

    print("Problem {}: {}".format(cnt, cost_data[N-1][N-1]))
    cnt += 1





