import sys
sys.stdin = open('input.txt')

def dfs(num, result):
    global ans_max, ans_min
    if num == N - 1:
        if ans_max < result:
            ans_max = result
        if ans_min > result:
            ans_min = result
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            if i == 0:
                dfs(num + 1, result + data[num + 1])
            elif i == 1:
                dfs(num + 1, result - data[num + 1])
            elif i == 2:
                dfs(num + 1, result * data[num + 1])
            elif i == 3:
                dfs(num + 1, int(result / data[num + 1]))
            cal[i] += 1

T = int(input())

for case in range(T):
    N = int(input())
    cal = list(map(int, input().split()))
    data = list(map(int, input().split()))
    ans_max = -987654321
    ans_min = 987654321
    dfs(0, data[0])

    print('#{} {}'.format(case + 1, ans_max - ans_min))
