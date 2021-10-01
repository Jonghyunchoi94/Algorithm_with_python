import sys
sys.stdin = open('input.txt')


T = int(input())

# row,column 델타 탐색 방향 : 우, 좌, 하, 상
dr = [0,0,1,-1]
dc = [1,-1,0,0]


# Core가 갈 수 있는 방향 판별
def Core_direction(r, c):
    res = []
    for i in range(r + 1, N):
        if data[i][c] != 0:
            break
    else:
        res.append(2)

    for i in range(r):
        if data[i][c] != 0:
            break
    else:
        res.append(3)

    for i in range(c + 1, N):
        if data[r][i] != 0:
            break
    else:
        res.append(0)

    for i in range(c):
        if data[r][i] != 0:
            break
    else:
        res.append(1)

    return res

# 방문 체크
def check_visit(r, c, n):
    cnt = 0
    if n == 2:
        for i in range(r + 1, N):
            cnt += 1
            data[i][c] = 2
    elif n == 3:
        for i in range(r):
            cnt += 1
            data[i][c] = 2
    elif n == 0:
        for i in range(c + 1, N):
            cnt += 1
            data[r][i] = 2
    elif n == 1:
        for i in range(c):
            cnt += 1
            data[r][i] = 2
    return cnt

# 방문 표시 지우는 백트래킹
def uncheck_visit(r, c, n):
    cnt = 0
    if n == 2:
        for i in range(r + 1, N):
            cnt -= 1
            data[i][c] = 0
    elif n == 3:
        for i in range(r):
            cnt -= 1
            data[i][c] = 0
    elif n == 0:
        for i in range(c + 1, N):
            cnt -= 1
            data[r][i] = 0
    elif n == 1:
        for i in range(c):
            cnt -= 1
            data[r][i] = 0
    return cnt


def dfs(pos):
    global ans, res, empty, emp
    if ans >= res and emp > empty:
        return

    if len(pos) == 0:
        if empty > emp:
            empty = emp
            res = ans
        else:
            if res > ans and empty >= emp:
                empty = emp
                res = ans

        return
    r, c = pos[0]

    if not Core_direction(r, c):
        emp += 1
        dfs(pos[1:])
        emp -= 1
    else:
        for k in Core_direction(r, c):
            cnt_cell = check_visit(r, c, k)
            ans += cnt_cell
            dfs(pos[1:])
            cnt_cell = uncheck_visit(r, c, k)
            ans += cnt_cell



for case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    res = 987654321
    ans = 0
    emp = 0
    empty = 13
    pos = []
    for i in range(N):
        for j in range(N):
            if (not (i == 0 or j == 0)) and data[i][j] == 1:
                pos.append([i, j])
    dfs(pos)
    print('#{} {}'.format(case + 1, res))
