import sys
sys.stdin = open('input.txt')

import math
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    k = math.isqrt(distance - 1)
    print(2 * k if distance <= k * (k + 1) else 2 * k + 1)