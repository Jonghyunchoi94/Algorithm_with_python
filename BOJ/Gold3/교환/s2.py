import sys
sys.stdin = open('input.txt')

N, K = sys.stdin.readline().split()
K = int(K)
N = list(map(int, N))


dp = [{} for _ in range(K+1)]
def dfs(num, cnt):
    global res
    if cnt == K:
        return int(''.join(map(str, num)))

    if int(''.join(map(str, num))) in dp[cnt]:
        return dp[cnt][int(''.join(map(str, num)))]

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if i == 0 and num[j] == 0:
                continue
            num[i], num[j] = num[j], num[i]
            temp = dfs(num, cnt + 1)
            num[i], num[j] = num[j], num[i]

            if int(''.join(map(str, num))) not in dp[cnt]:
                dp[cnt][int(''.join(map(str, num)))] = temp
            else:
                dp[cnt][int(''.join(map(str, num)))] = max(dp[cnt][int(''.join(map(str, num)))], temp)
    return dp[cnt][int(''.join(map(str, num)))]


if (len(N) == 2 and N[1] == 0) or len(N) == 1:
    print(-1)
else:
    print(dfs(N, 0))
