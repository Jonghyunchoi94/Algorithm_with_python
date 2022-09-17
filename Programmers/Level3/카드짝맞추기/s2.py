board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r = 1
c = 0


from collections import deque, defaultdict

def cardinfo(road):
    cardlist, cardpos = [], defaultdict(list)
    for i in range(len(road)):
        for j in range(len(road[0])):
            if road[i][j] != 0:
                cardpos[road[i][j]].append((i, j))
                if road[i][j] not in cardlist:
                    cardlist.append(road[i][j])
    return cardlist, cardpos


def solution(board, r, c):
    answer = 987654321

    card, pos = cardinfo(board)
    # print(card)
    # print(pos)

    visited = [0] * len(card)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def bfs(row, column, num):
        pq = deque([(row, column, 0, 0)])

        while pq:
            x, y, turn, cnt = pq.popleft()
            if board[x][y] == num and cnt == 1:
                board[x][y] = 0
                return x, y, turn + 2
            elif board[x][y] == num:
                board[x][y] = 0
                pq.clear()
                cnt = 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                rx = x + dx[k]
                ry = y + dy[k]

                if dx[k] > 0:
                    while rx < len(board) - 1:
                        if board[rx][ry] != 0:
                            break
                        rx += 1
                elif dx[k] < 0:
                    while rx > 0:
                        if board[rx][ry] != 0:
                            break
                        rx -= 1
                elif dy[k] > 0:
                    while ry < len(board[0]) - 1:
                        if board[rx][ry] != 0:
                            break
                        ry += 1
                elif dy[k] < 0:
                    while ry > 0:
                        if board[rx][ry] != 0:
                            break
                        ry -= 1

                if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                    pq.append((nx, ny, turn + 1, cnt))

                if 0 <= rx < len(board) and 0 <= ry < len(board[0]):
                    if nx != rx or ny != ry:
                        pq.append((rx, ry, turn + 1, cnt))

    def dfs(n, row, column, cnt):
        nonlocal answer
        if n == len(visited):
            if answer > cnt:
                answer = cnt
            return

        for i in range(len(visited)):
            if visited[i] == 0:
                visited[i] = 1
                nr, nc, ans = bfs(row, column, card[i])
                dfs(n + 1, nr, nc, cnt + ans)
                for k, l in pos[card[i]]:
                    board[k][l] = card[i]
                visited[i] = 0

    dfs(0, r, c, 0)

    return answer


print(solution(board, r, c))