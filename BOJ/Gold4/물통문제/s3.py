import sys
sys.stdin = open('input.txt')

import math

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    gcd = math.gcd(a, b)
    if (gcd == 1) or (c % gcd == 0):
        print("YES")
    else:
        print("NO")
