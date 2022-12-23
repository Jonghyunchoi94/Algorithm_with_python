import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

data = [0] * 301
for i in range(N):
    info = int(sys.stdin.readline().rstrip())
    data[i] = info
dp = [-1] * 301

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[0] + data[2], data[1] + data[2])

for i in range(3, N):
    dp[i] = max(dp[i - 2] + data[i], dp[i - 3] + data[i - 1] + data[i])

print(dp[N - 1])