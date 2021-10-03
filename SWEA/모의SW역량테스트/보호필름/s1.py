import sys
sys.stdin = open('input.txt')

def test_pass(column):
    res = 0
    cur = data[0][column]
    for i in range(D):
        if res >= K:
            break

        temp = data[i][column]
        if temp == cur:
            res += 1
        else:
            cur = data[i][column]
            res = 0
    else:
        return False
    return True

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


def dfs(t, change):
    if t == W:
        return

    for i in range(s, D):






T = int(input())

for case in range(T):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]

    for c in range(W):
        if not test_pass(c):
            break
    else:
        print('#{} {}'.format(case + 1, 0))




