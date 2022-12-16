import sys
sys.stdin = open('input.txt')

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

graph = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
num_cnt = (c2 - c1 + 1) * (r2 - r1 + 1)

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

s = 1
Flag = 0
step = 1
r, c, idx = 0, 0, 0

while num_cnt > 0:
    if Flag == 2:
        Flag = 0
        step += 1
    for _ in range(step):
        if r1 <= r <= r2 and c1 <= c <= c2:
            graph[r - r1][c - c1] = s
            num_cnt -= 1
            max_num = s

        r, c = r + dr[idx % 4], c + dc[idx % 4]
        s += 1

    Flag += 1
    idx += 1

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(graph[i][j]).rjust(len(str(max_num))), end=' ')
    print()