import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    res = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())

        dist1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        dist2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5

        if (dist1 > r and dist2 < r) or (dist1 < r and dist2 > r):
            res += 1

    print(res)

