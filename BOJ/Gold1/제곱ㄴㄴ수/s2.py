import sys
import math
sys.stdin = open('input.txt')

a, b = map(int, sys.stdin.readline().split())

aa = math.isqrt(a)
bb = math.isqrt(b)


cnt = b - a + 1
status = [False] * cnt

for i in range(2, bb + 1):
    s = i ** 2
    for j in range((((a - 1)//s) + 1) * s, b + 1, s):
        if not status[j - a]:
            status[j - a] = True
            cnt -= 1
print(cnt)
