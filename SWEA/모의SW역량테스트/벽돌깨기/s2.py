import sys
sys.stdin = open('input.txt')

from copy import deepcopy

def find_not_empty(cur_data, column):
    res = H
    for i in range(H):
        if cur_data[i][column]:
            res = i
            break
    return res

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def change_data(visit_data, cur_data):
    for r, c in visit_data:
        cur_data[r][c] = 0
        idx = r - 1
        while idx >= 0:
            if cur_data[idx][c] != 0:
                cur_data[r][c], cur_data[idx][c] = cur_data[idx][c], cur_data[r][c]
                r = idx
            else:
                break
            idx -= 1
    return cur_data


def start_point(r, c, value):
    global visited
    visited.add((r, c))
    for k in range(4):
        next_r = r + dr[k]
        next_c = c + dc[k]
        if 0 <= next_r < H and 0 <= next_c < W and value > 1 and visit[next_r][next_c] == 0:
            visit[next_r][next_c] = 1
            start_point(next_r, next_c, value - 1)
            visit[next_r][next_c] = 0

def count(data):
    res = 0
    for i in range(H):
        for j in range(W):
            if data[i][j] != 0:
                res += 1
    return res

def try_combination(tr, cur_data):
    global visited, answer, number
    visited = set()
    if tr == N:
        if answer > count(cur_data):
            answer = count(cur_data)
        return

    for i in range(W):
        if find_not_empty(cur_data, i) < H:
            temp = deepcopy(cur_data)
            start_point(find_not_empty(cur_data, i), i, cur_data[find_not_empty(cur_data, i)][i])
            sort_visited = sorted(list(visited), key = lambda x:(x[0],x[1]))
            new_data = change_data(sort_visited, temp)
            try_combination(tr + 1, new_data)




T = int(input())

for case in range(T):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    answer = 987654321
    number = 0
    try_combination(0, data)

    print(answer)
