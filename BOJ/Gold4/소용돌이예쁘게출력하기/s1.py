import sys
sys.stdin = open('input.txt')

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

max_level = max(abs(r1), abs(c1), abs(r2), abs(c2))
graph = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]
max_num = 0


for l in range(max_level - 50, max_level + 1):
    pos = [l, l]
    val = (2 * l + 1) ** 2

    if l == 0:
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            graph[pos[0] - r1][pos[1] - c1] = val
            continue

    for i1 in range(l * 2):
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            graph[pos[0] - r1][pos[1] - c1] = val
            max_num = max(max_num, val)
        pos[1] -= 1
        val -= 1

    for i2 in range(l * 2):
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            graph[pos[0] - r1][pos[1] - c1] = val
            max_num = max(max_num, val)
        pos[0] -= 1
        val -= 1

    for i3 in range(l * 2):
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            graph[pos[0] - r1][pos[1] - c1] = val
            max_num = max(max_num, val)
        pos[1] += 1
        val -= 1

    for i4 in range(l * 2):
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            graph[pos[0] - r1][pos[1] - c1] = val
            max_num = max(max_num, val)
        pos[0] += 1
        val -= 1

for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        print(str(graph[i][j]).rjust(len(str(max_num))), end=' ')
    print()



