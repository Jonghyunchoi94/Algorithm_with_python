import sys
sys.stdin = open('input.txt')

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

max_idx = max(abs(r1), abs(c1), abs(r2), abs(c2))
n = max_idx * 2 + 1
max_num = n ** 2
graph = [[0] * n for _ in range(n)]

s = 2
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
r, c = n // 2, n // 2
graph[r][c] = 1
Flag = 0
step = 1
idx = 0
while max_num > s:
    if Flag == 2:
        Flag = 0
        step += 1
    for _ in range(step):
        nr, nc = r + dr[idx % 4], c + dc[idx % 4]
        graph[nr][nc] = s
        r, c = nr, nc
        s += 1
        if s > max_num:
            break
    Flag += 1
    idx += 1


r1 += max_idx
c1 += max_idx
r2 += max_idx
c2 += max_idx
# print(graph)
# print(r1, c1, r2, c2)
def tranform(num, max_len):
    s = str(num)
    if len(s) == max_len:
        return s
    else:
        return ' ' * (max_len - len(s)) + s

for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        print(tranform(graph[i][j], len(str(max_num))), end=' ')
    print()