board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0

# 14
"""
단순 BFS로는 시간초과
DP를 이용하거나 비트마스킹을 써서 해결해야할 듯합니다
주말을 이용해 비트마스킹 공부 요망!!
"""

from itertools import permutations, product
from collections import defaultdict, deque
from copy import deepcopy

class Movement(object):
    def __init__(self, data, r, c, direction, cnt=0):
        super(Movement, self).__init__()
        self.data = data
        self.r = r
        self.c = c
        self.direction = direction
        self.cnt = cnt
        self.dr = [0, 0, 1, -1]
        self.dc = [1, -1, 0, 0]

    def shortmove(self):
        if self.direction == 0 and self.c >= 3:
            return self.r, self.c, self.cnt
        elif self.direction == 1 and self.c <= 0:
            return self.r, self.c, self.cnt
        elif self.direction == 2 and self.r >= 3:
            return self.r, self.c, self.cnt
        elif self.direction == 3 and self.r <= 0:
            return self.r, self.c, self.cnt
        else:
            self.r = self.r + self.dr[self.direction]
            self.c = self.c + self.dc[self.direction]
            self.cnt = self.cnt + 1
        return self.r, self.c, self.cnt

    def ctrlmove(self):
        if self.direction == 0 and self.c >= 3:
            return self.r, self.c, self.cnt
        elif self.direction == 1 and self.c <= 0:
            return self.r, self.c, self.cnt
        elif self.direction == 2 and self.r >= 3:
            return self.r, self.c, self.cnt
        elif self.direction == 3 and self.r <= 0:
            return self.r, self.c, self.cnt
        else:
            while True:
                if self.direction == 0 and self.c >= 3:
                    break
                elif self.direction == 1 and self.c <= 0:
                    break
                elif self.direction == 2 and self.r >= 3:
                    break
                elif self.direction == 3 and self.r <= 0:
                    break
                self.r = self.r + self.dr[self.direction]
                self.c = self.c + self.dc[self.direction]
                if self.data[self.r][self.c] != 0:
                    break
            self.cnt = self.cnt + 1
        return self.r, self.c, self.cnt

def bfs(data, x, y, goal_x, goal_y):
    cnt = 0
    q = deque()
    q.append((x, y, 0))
    visited = set()
    visited.add((x, y, 0))
    while q:
        r, c, n = q.popleft()
        # print(data)
        if (r, c) == (goal_x, goal_y):
            data[r][c] = 0
            cnt = n
            break
        for k in range(4):
            temp1 = Movement(data, r, c, k, n)
            a = temp1.shortmove()
            if a not in visited:
                q.append(a)
                visited.add(a)
            # print("{}".format(q))
            temp2 = Movement(data, r, c, k, n)
            b = temp2.ctrlmove()
            if b not in visited:
                q.append(b)
                visited.add(b)
            # print("{}".format(q))
    return data, cnt


def solution(board, r, c):
    number_list = []
    position = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                position[board[i][j]].append((i, j))
                if board[i][j] not in number_list:
                    number_list.append(board[i][j])

    case = list(permutations(number_list, len(number_list)))
    # print(case)
    # print(position)
    idx_permutation = [[(0, 1), (1, 0)] for _ in range(len(number_list))]
    idx_permutation = list(product(*idx_permutation))
    # print(idx_permutation)

    res = 987654321
    al = 0
    while al < len(case):
        t = 0
        while t < len(idx_permutation):
            for k in idx_permutation:
                temp_r, temp_c = r, c
                copydata = deepcopy(board)
                cnt = 0
                f = 0
                for l in k:
                    if cnt >= res:
                        break
                    for m in l:
                        result_data, result_cnt = bfs(copydata, temp_r, temp_c,\
                                          position[case[al][f]][m][0], position[case[al][f]][m][1])
                        cnt += result_cnt
                        # print("{} : {}".format(k, cnt))
                        copydata = result_data
                        # print(copydata)
                        temp_r, temp_c = position[case[al][f]][m][0], position[case[al][f]][m][1]
                        # print(temp_r, temp_c)
                    f += 1
                cnt += (len(number_list) * 2)
                res = min(res, cnt)
                t += 1
        al += 1
    return res

print(solution(board, r, c))