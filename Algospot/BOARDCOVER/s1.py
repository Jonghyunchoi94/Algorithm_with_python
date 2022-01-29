import sys

sys.stdin = open('input.txt')

"""
문제 접근
1. 블록을 기준으로 만들 수 있는 모양 특정
2. 순서가 겹치지 않게 기준을 정해놓는다. (여기서는 위쪽 그 다음으로는 왼쪽을 기준)

"""

cover_type = [[[0, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [1, -1]]]


def map_set(board, x, y, type, delta):
    ok = True
    for i in range(3):
        next_x = x + cover_type[type][i][0]
        next_y = y + cover_type[type][i][1]

        if next_x < 0 or next_x >= len(board) or next_y < 0 or next_y >= len(board[0]):
            ok = False

        else:
            board[next_x][next_y] += delta
            if board[next_x][next_y] > 1:
                ok = False
    return ok


def cover(data_array):
    x = y = -1
    for i in range(len(data_array)):
        for j in range(len(data_array[i])):
            if data_array[i][j] == 0:
                x = i
                y = j
                break
        if x != -1:
            break

    if x == -1:
        return 1

    ret = 0

    for t in range(4):
        if map_set(data_array, x, y, t, 1):
            ret += cover(data_array)

        map_set(data_array, x, y, t, -1)

    return ret


C = int(input())

for case in range(C):
    H, W = map(int, input().split())
    block = [list(input()) for _ in range(H)]
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j] == ".":
                block[i][j] = 0
            else:
                block[i][j] = 5
    print(cover(block))