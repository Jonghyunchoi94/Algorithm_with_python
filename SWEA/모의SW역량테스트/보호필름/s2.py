import sys
sys.stdin = open('input.txt')

def test_pass(data):
    ans = 0
    for c in range(W):
        res = 0
        cur = data[0][c]
        for r in range(D):
            temp = data[r][c]
            if temp == cur:
                res += 1
            else:
                cur = data[r][c]
                res = 1
            if res >= K:
                ans += 1
                break
    if ans == W:
        return True
    else:
        return False



def medicine_A(row):
    for i in range(W):
        data[row][i] = 0

def medicine_B(row):
    for i in range(W):
        data[row][i] = 1

def un_medicine(row):
    res = []
    for i in range(W):
        res.append(data[row][i])
    return res


def dfs(change, s):
    global ans
    if change > ans:
        return

    if test_pass(data):
        if ans > change:
            ans = change
        return

    for i in range(s, D):
        temp = un_medicine(i)
        medicine_A(i)
        dfs(change + 1, s + 1)
        medicine_B(i)
        dfs(change + 1, s + 1)
        data[i] = temp






T = int(input())

for case in range(T):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]
    ans = 987654321
    if test_pass(data):
        print('#{} {}'.format(case + 1, 0))
    else:
        dfs(0, 0)
        print('#{} {}'.format(case + 1, ans))

