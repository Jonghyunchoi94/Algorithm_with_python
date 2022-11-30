import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    cnt = 0
    pos = set()
    x, y = 0, r1
    while y >= 0:
        pos.add((x1 + x, y1 + y))
        pos.add((x1 + x, y1 - y))
        pos.add((x1 - x, y1 + y))
        pos.add((x1 - x, y1 - y))
        x += 1
        y -= 1

    for i, j in pos:
        if abs(x2 - i) + abs(y2 - j) == r2:
            cnt += 1

    print(cnt)