import sys
import math
sys.stdin = open('input.txt')

a, b = map(int, sys.stdin.readline().split())

aa = math.isqrt(a)
bb = math.isqrt(b)

total_cnt = b - a + 1
s = 2
res = 0
while bb >= s:
    for i in range(s ** 2, b + 1, s ** 2):
        if i >= a:
            res += 1
    s += 1


print(total_cnt - res)