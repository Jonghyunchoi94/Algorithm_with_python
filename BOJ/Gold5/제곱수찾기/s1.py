import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

graph = []

for i in range(N):
    row = sys.stdin.readline().rstrip()
    graph.append(row)

res = -1
for r in range(N):
    for c in range(M):
        for m in range(-N, N):
            for n in range(-M, M):
                if m == 0 and n == 0:
                    continue
                step = 0
                x, y = r, c
                val = ''

                while 0 <= x < N and 0 <= y < M:
                    val += graph[x][y]
                    step += 1

                    val_int = int(''.join(val))
                    val_sqrt = val_int ** 0.5
                    val_is_sqrt = val_sqrt - int(val_sqrt)
                    if val_is_sqrt == 0 and val_int > res:
                        res = val_int

                    x = r + step * m
                    y = c + step * n

print(res)
