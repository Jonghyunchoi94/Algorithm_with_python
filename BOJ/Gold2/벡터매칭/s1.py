import sys
sys.stdin = open('input.txt')
import math
from itertools import combinations

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    l = []
    total_x = 0
    total_y = 0
    res = math.inf
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        total_x += x
        total_y += y
        l.append((x, y))

    cnt = len(l)
    case = list(combinations(l, N // 2))
    ll = len(case) // 2

    for i in case[:ll]:
        i = list(i)


        total_x1 = 0
        total_y1 = 0
        for x1, y1 in i:
            total_x1 += x1
            total_y1 += y1
        total_x2 = total_x - total_x1
        total_y2 = total_y - total_y1

        res = min(res, math.sqrt((total_x1 - total_x2) ** 2 + (total_y1 - total_y2) ** 2))

    print(res)