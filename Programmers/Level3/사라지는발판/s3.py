board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
aloc = [1, 0]
bloc = [1, 2]

from copy import deepcopy

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def Can_Go(x, y, road):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or nx >= len(road) or ny < 0 or ny >= len(road[0]) or road[nx][ny] == 0:
            pass
        else:
            return True

    return False

def Aturn(road, x1, y1, x2, y2, turn):
    Flag = False
    winner = []
    loser = []
    if road[x1][y1] == 0:
        return (-1, turn)


    for k in range(4):
        nx = x1 + dx[k]
        ny = y1 + dy[k]
        if nx < 0 or nx >= len(road) or ny < 0 or ny >= len(road[0]) or road[nx][ny] == 0:
            continue
        road[x1][y1] = 0
        ret = Bturn(road, nx, ny, x2, y2, turn + 1)
        road[x1][y1] = 1

        if ret[0] == -1:
            winner.append(ret[1])
        else:
            loser.append(ret[1])
        Flag = True
    if Flag:
        if winner:
            return (1, min(winner))
        else:
            return (-1, max(loser))
    else:
        return (-1, turn)

def Bturn(road, x1, y1, x2, y2, turn):
    Flag = False
    winner = []
    loser = []
    if not Can_Go(x2, y2, road):
        return (-1 ,turn)
    # if road[x2][y2] == 0:
    #     return (-1, turn)

    for k in range(4):
        nx = x2 + dx[k]
        ny = y2 + dy[k]
        if nx < 0 or nx >= len(road) or ny < 0 or ny >= len(road[0]) or road[nx][ny] == 0:
            continue
        road[x2][y2] = 0
        ret = Aturn(road, x1, y1, nx, ny, turn + 1)
        road[x2][y2] = 1

        if ret[0] == -1:
            winner.append(ret[1])
        else:
            loser.append(ret[1])
        Flag = True
    if Flag:
        if winner:
            return (1, min(winner))
        else:
            return (-1, max(loser))
    else:
        return (-1, turn)




def solution(board, aloc, bloc):
    road = deepcopy(board)

    answer = Aturn(road, aloc[0], aloc[1], bloc[0], bloc[1], 0)

    return answer[1]

print(solution(board, aloc, bloc))