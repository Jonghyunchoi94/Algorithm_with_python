import sys
sys.stdin = open('input.txt')

N = int(input())

P = list(map(int, input().split()))

P.sort()

ans = 0
tmp = 0
for i in P:
    tmp += i
    ans += tmp

print(ans)