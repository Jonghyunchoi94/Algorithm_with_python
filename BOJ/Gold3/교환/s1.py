import sys
sys.stdin = open('input.txt')

N, K = sys.stdin.readline().split()
K = int(K)
N = list(map(int, N))

res = -1

def dfs(num, cnt):
    global res
    if cnt == 0:
        res = max(res, int(''.join(map(str, num))))
        return

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if i == 0 and num[j] == 0:
                continue
            num[i], num[j] = num[j], num[i]
            dfs(num, cnt - 1)
            num[i], num[j] = num[j], num[i]



dfs(N, K)
print(res)
