board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

def solution(board, skill):
    answer = 0

    road = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]


    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            road[r1][c1] -= degree
            road[r1][c2 + 1] += degree
            road[r2 + 1][c1] += degree
            road[r2 + 1][c2 + 1] -= degree
        else:
            road[r1][c1] += degree
            road[r1][c2 + 1] -= degree
            road[r2 + 1][c1] -= degree
            road[r2 + 1][c2 + 1] += degree

    # 행 누적합
    for r in range(len(road) - 1):
        for c in range(len(road[0]) - 1):
            road[r][c + 1] += road[r][c]

    # 열 누적합
    for c in range(len(road[0]) - 1):
        for r in range(len(road) - 1):
            road[r + 1][c] += road[r][c]


    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += road[r][c]
            if board[r][c] > 0:
                answer += 1

    return answer


print(solution(board, skill))