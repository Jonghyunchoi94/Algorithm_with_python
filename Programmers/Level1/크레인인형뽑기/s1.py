board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


# 인덱스 0 -> 1

def solution(board, moves):
    answer = 0

    rot_board = [list(i) for i in zip(*board)]
    q = []
    for m in moves:
        i = 0
        while rot_board[m - 1][i] == 0:
            i += 1
            if i >= len(board):
                break
        if i < len(board):
            q.append(rot_board[m - 1][i])
            rot_board[m - 1][i] = 0

        if len(q) >= 2 and q[-1] == q[-2]:
            q.pop()
            q.pop()
            answer += 2

    return answer

print(solution(board, moves))