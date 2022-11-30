import sys
sys.stdin = open('input.txt')

T = int(input())

"""
r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
r1 + r2 = d 이면 두 원은 외접한다.
|r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
|r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.
"""


for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if distance == 0 and r1 == r2:
        print(-1)
    elif abs(r1 - r2) == distance or r1 + r2 == distance:
        print(1)
    elif abs(r1 - r2) < distance < r1 + r2:
        print(2)
    else:
        print(0)