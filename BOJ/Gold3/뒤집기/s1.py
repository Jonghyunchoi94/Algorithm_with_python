import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
pic = [list(input()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count = 0
answer = 0

for i in range(N):
    for j in range(M):
        for k in range(4):
            next_x = i + dx[k]
            next_y = j + dy[k]

            if 0 <= next_x < N and 0 <= next_y < M:
                if pic[i][j] != pic[next_x][next_y]:
                    count += 1
                    break

answer = pow(2, N * M - count) % 1000000007

print(answer)