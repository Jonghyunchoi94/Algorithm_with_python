board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

from collections import deque

straight = [(0, 1), (0, -1), (-1, 0), (1, 0)]
h_rotate_1 = [(1, 1), (-1, 1)]
h_rotate_2 = [(-1, -1), (1, -1)]
v_rotate_1 = [(1, 1), (1, -1)]
v_rotate_2 = [(-1, -1), (-1, 1)]

def solution(board):
    answer = 0
    n = len(board) - 1
    left = (0, 0)
    right = (0, 1)
    pq = deque([(left, right, 0)])
    visited = set()

    while pq:
        l, r, time = pq.popleft()
        # print(l, r, time)
        if (l, r) in visited:
            continue
        visited.add((l, r))
        if (l == (n, n)) or (r == (n, n)):
            answer = time
            break

        for k in range(4):
            nl, nr = (l[0] + straight[k][0], l[1] + straight[k][1]), (r[0] + straight[k][0], r[1] + straight[k][1])

            if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0 and board[nr[0]][nr[1]] == 0:
                pq.append((nl, nr, time + 1))

        if l[0] == r[0] and l[1] < r[1]:
            for k in range(2):
                nl, nr = (l[0] + h_rotate_1[k][0], l[1] + h_rotate_1[k][1]), (r[0], r[1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][
                    nl[1]] == 0:
                    if board[l[0] + h_rotate_1[k][0]][l[1]] == 0:
                        pq.append((nl, nr, time + 1))
            for k in range(2):
                nl, nr = (l[0], l[1]), (r[0] + h_rotate_2[k][0], r[1] + h_rotate_2[k][1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nr[0]][nr[1]] == 0:
                    if board[r[0] + h_rotate_2[k][0]][r[1]] == 0:
                        pq.append((nl, nr, time + 1))
        elif l[0] == r[0] and l[1] > r[1]:
            for k in range(2):
                nl, nr = (l[0] + h_rotate_2[k][0], l[1] + h_rotate_2[k][1]), (r[0], r[1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0:
                    if board[l[0] + h_rotate_2[k][0]][l[1]] == 0:
                        pq.append((nl, nr, time + 1))
            for k in range(2):
                nl, nr = (l[0], l[1]), (r[0] + h_rotate_1[k][0], r[1] + h_rotate_1[k][1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nr[0]][nr[1]] == 0:
                    if board[r[0] + h_rotate_1[k][0]][r[1]] == 0:
                        pq.append((nl, nr, time + 1))
        elif l[1] == r[1] and l[0] < r[0]:
            for k in range(2):
                nl, nr = (l[0] + v_rotate_1[k][0], l[1] + v_rotate_1[k][1]), (r[0], r[1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0:
                    if board[l[0]][l[1] + v_rotate_1[k][1]] == 0:
                        pq.append((nl, nr, time + 1))
            for k in range(2):
                nl, nr = (l[0], l[1]), (r[0] + v_rotate_2[k][0], r[1] + v_rotate_2[k][1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nr[0]][nr[1]] == 0:
                    if board[r[0]][r[1] + v_rotate_2[k][1]] == 0:
                        pq.append((nl, nr, time + 1))
        elif l[1] == r[1] and l[0] > r[0]:
            for k in range(2):
                nl, nr = (l[0] + v_rotate_2[k][0], l[1] + v_rotate_2[k][1]), (r[0], r[1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nl[0]][nl[1]] == 0:
                    if board[l[0]][l[1] + v_rotate_2[k][1]] == 0:
                        pq.append((nl, nr, time + 1))
            for k in range(2):
                nl, nr = (l[0], l[1]), (r[0] + v_rotate_1[k][0], r[1] + v_rotate_1[k][1])

                if 0 <= nl[0] <= n and 0 <= nl[1] <= n and 0 <= nr[0] <= n and 0 <= nr[1] <= n and board[nr[0]][nr[1]] == 0:
                    if board[r[0]][r[1] + v_rotate_1[k][1]] == 0:
                        pq.append((nl, nr, time + 1))

    return answer

print(solution(board))