import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort(reverse=True)
B.sort()
res = 0
for i in range(N):
    res += A[i] * B[i]

print(res)