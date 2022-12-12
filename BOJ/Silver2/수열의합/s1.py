import sys
sys.stdin = open('input.txt')

N, L = map(int, sys.stdin.readline().split())

def sum_num(num):
    res = 0
    for h in range(num):
        res += h
    return res

s = L
ans = []
temp1 = 0
while True:
    if (N - sum_num(s)) < 0 or s > 100:
        temp1 = -1
        break
    if (N - sum_num(s)) % s == 0:
        temp1 = (N - sum_num(s)) // s
        break
    s += 1

if temp1 == -1:
    print(-1)
else:
    for i in range(s):
        temp2 = temp1 + i
        ans.append(temp2)
    print(" ".join(map(str, ans)))