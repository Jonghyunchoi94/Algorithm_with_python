rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

from collections import deque
from copy import deepcopy
def make_road(road, x1, y1, x2, y2):
    answer = [[road[i][j] for j in range(y1 - 1, y2)] for i in range(x1 - 1, x2)]
    num = 987654321
    for r in range(len(answer)):
        for c in range(len(answer[0])):
            if r == 0 or r == len(answer) - 1 or c == 0 or c == len(answer[0]) - 1:
                if answer[r][c] < num:
                    num = answer[r][c]
    return answer, num

def recover_road(road, temp, x1, y1, x2, y2):
    answer = deepcopy(road)
    t = [temp[i][j] for i in range(len(temp)) for j in range(len(temp[0]))]

    s = 0

    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            answer[i][j] = t[s]
            s += 1
    return answer

def solution(rows, columns, queries):
    answer = []

    road = [[0] * columns for _ in range(rows)]

    temp = 1
    for i in range(rows):
        for j in range(columns):
            road[i][j] = temp
            temp += 1
    # print(road)

    for x1, y1, x2, y2 in queries:
        temp, min_num = make_road(road, x1, y1, x2, y2)
        answer.append(min_num)
        ntemp = []
        left, mid, right = deque(), deque(), deque()
        for r in range(x2 - x1 + 1):
            left.append(temp[r][0])
            right.append(temp[r][-1])
            tmp = deque(temp[r][1:y2 - y1])
            mid.append(tmp)

        x = left.popleft()
        mid[0].appendleft(x)
        x = mid[0].pop()
        right.appendleft(x)
        x = right.pop()
        mid[-1].append(x)
        x = mid[-1].popleft()
        left.append(x)

        for nr in range(x2 - x1 + 1):
            ntemp.append([])
            ntemp[-1].append(left.popleft())
            ntemp[-1].extend(mid.popleft())
            ntemp[-1].append(right.popleft())

        road = recover_road(road, ntemp, x1, y1, x2, y2)

    return answer

print(solution(rows, columns, queries))