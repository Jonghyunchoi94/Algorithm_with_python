import sys
sys.stdin = open('input.txt')

from copy import deepcopy


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def find_not_empty(have, column):
    res = H - 1
    for i in range(H):
        if have[i][column]:
            res = i
            break
    return res

def change_data(visit_data, memory):
    for r, c in visit_data:
        memory[r][c] = 0
        idx = r - 1
        while idx >= 0:
            if memory[idx][c] != 0:
                memory[r][c], memory[idx][c] = memory[idx][c], memory[r][c]
                r = idx
            else:
                break
            idx -= 1
    return memory


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

def try_combination(tr, cur_data, col, cnt):
    global visited, answer
    visited = set()
    if col > W:
        return

    if tr == N:
        if answer < cnt:
            answer = cnt
        return

    for i in range(W):
        try_combination(tr, cur_data, col + 1, cnt)
        change = deepcopy(cur_data)
        start_point(find_not_empty(cur_data, col), col, cur_data[find_not_empty(cur_data, col)][col])
        sort_visited = sorted(list(visited), key=lambda x: (x[0], x[1]))
        new_data = change_data(sort_visited, change)
        try_combination(tr + 1, new_data, col + 1, cnt + len(sort_visited))



T = int(input())

for case in range(T):
    N, W, H = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(H)]
    visit = [[0] * W for _ in range(H)]
    answer = 0

    try_combination(0, data, 0, 0)
    print(answer)
