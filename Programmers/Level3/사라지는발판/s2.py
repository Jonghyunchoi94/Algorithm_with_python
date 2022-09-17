board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def possible_to_go(x, y, road):
    Flag = False

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= len(road) or ny < 0 or ny >= len(road[0]) or road[nx][ny] == 0:
            continue
        else:
            Flag = True

    return Flag


def solution(board, aloc, bloc):
    winner = []
    loser = []
    ans = 0
    res = "A"

    tmp = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                tmp[i][j] = 1

    # visited = [[0] * len(board[0]) for _ in range(len(board))]

    def dfs(x1, y1, x2, y2, player, turn):
        nonlocal winner, loser, res, ans
        flag = False
        if player == "A" and (not possible_to_go(x1, y1, tmp)):
            loser.append(turn)
            return
        elif player == "B" and (not possible_to_go(x2, y2, tmp)):
            winner.append(turn)
            return

        for k in range(4):
            if player == "A":
                nx = x1 + dx[k]
                ny = y1 + dy[k]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or tmp[nx][ny] == 0:
                    continue
                # visited[nx][ny] = 1
                tmp[x1][y1] = 0
                dfs(nx, ny, x2, y2, "B", turn + 1)
                tmp[x1][y1] = 1
            elif player == "B":
                nx = x2 + dx[k]
                ny = y2 + dy[k]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]) or tmp[nx][ny] == 0:
                    continue
                # visited[nx][ny] = 1
                tmp[x2][y2] = 0
                dfs(x1, y1, nx, ny, "A", turn + 1)
                tmp[x2][y2] = 1
            flag = True
        if flag:
            if winner:
                if player == "A":
                    ans = max(loser)
                    return
                else:
                    ans = min(winner)
                    return

        return
    dfs(aloc[0], aloc[1], bloc[0], bloc[1], "A", 0)

    return ans

print(solution(board, aloc, bloc))
