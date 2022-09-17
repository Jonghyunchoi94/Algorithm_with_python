board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]


def roadmap(r1, c1, r2, c2):
    res = []
    for row in range(r1, r2 + 1):
        for column in range(c1, c2 + 1):
            res.append((row, column))
    return res



def solution(board, skill):
    answer = 0

    for type, r1, c1, r2, c2, degree in skill:
        for r, c in roadmap(r1, c1, r2, c2):
            if type == 1:
                board[r][c] -= degree
            else:
                board[r][c] += degree

    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] > 0:
                answer += 1


    return answer

print(solution(board, skill))