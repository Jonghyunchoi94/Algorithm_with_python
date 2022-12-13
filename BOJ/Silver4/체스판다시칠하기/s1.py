import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())

choice1 = 'BWBWBWBW'
choice2 = 'WBWBWBWB'

def change_count(choice, string):
    cnt = 0
    for i in range(8):
        if choice[i] != string[i]:
            cnt += 1
    return cnt

chess = []
res = 987654321
for _ in range(N):
    row = sys.stdin.readline().rstrip()
    chess.append(row)

def dfs(r, c, cnt, status, change):
    global res
    if cnt == 8:
        res = min(res, change)
        return

    temp = chess[r + cnt][c: c + 8]
    temp_cnt = change_count(status, temp)
    if status == choice1:
        dfs(r, c, cnt + 1, choice2, change + temp_cnt)
    else:
        dfs(r, c, cnt + 1, choice1, change + temp_cnt)
    return


for i in range(N - 7):
    for j in range(M - 7):
        dfs(i, j, 0, choice1, 0)
        dfs(i, j, 0, choice2, 0)

print(res)
