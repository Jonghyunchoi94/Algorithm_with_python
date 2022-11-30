board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

from collections import deque

straight = [(0, 1), (1, 0)]
rotate = (1, 1)

def solution(board):
    answer = 0
    n = len(board) - 1
    left = (0, 0)
    right = (0, 1)
    pq = deque([(left, right, 0)])

    while pq:
        l, r, time = pq.popleft()
        print(l, r, time)
        if (l == (n, n)) or (r == (n, n)):
            print(time)
            break

        for k in range(2):
            nl, nr = (l[0] + straight[k][0], l[1] + straight[k][1]), (r[0] + straight[k][0], r[1] + straight[k][1])

            if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0 and board[nr[0]][nr[1]] == 0:
                pq.append((nl, nr, time + 1))

        nl, nr = (l[0] + rotate[0], l[1] + rotate[1]), (r[0], r[1])

        if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0 and board[nr[0]][nr[1]] == 0:
            if board[l[0] + rotate[0]][l[1]] == 0:
                pq.append((nl, nr, time + 1))


    return answer

print(solution(board))