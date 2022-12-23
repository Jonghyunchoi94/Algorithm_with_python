import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
res = 0
data = []
for _ in range(N):
    info = int(sys.stdin.readline())
    data.append(info)

def dfs(num, status, score):
    global res
    if num >= N - 1:
        if num == N - 1:
            res = max(res, score + data[num - 1])
        else:
            res = max(res, score)
        return
    if status == 1:
        dfs(num + 2, 0, score + data[num - 1])
    else:
        dfs(num + 1, 1, score + data[num - 1])
        dfs(num + 2, 0, score + data[num - 1])

dfs(1, 0, data[0])
print(res)