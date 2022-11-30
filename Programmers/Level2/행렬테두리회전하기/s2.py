rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


from copy import deepcopy

def rotate(road, x1, y1, x2, y2):
    answer = deepcopy(road)
    min_num = 987654321
    for i in range(y1, y2):
        answer[x1 - 1][i] = road[x1 - 1][i - 1]
        if answer[x1 - 1][i] < min_num:
            min_num = answer[x1 - 1][i]

    for i in range(x1, x2):
        answer[i][y2 - 1] = road[i - 1][y2 - 1]
        if answer[i][y2 - 1] < min_num:
            min_num = answer[i][y2 - 1]

    for i in range(y1 - 1, y2 - 1):
        answer[x2 - 1][i] = road[x2 - 1][i + 1]
        if answer[x2 - 1][i] < min_num:
            min_num = answer[x2 - 1][i]

    for i in range(x1 - 1, x2 - 1):
        answer[i][y1 - 1] = road[i + 1][y1 - 1]
        if answer[i][y1 - 1] < min_num:
            min_num = answer[i][y1 - 1]

    return answer, min_num

def solution(rows, columns, queries):
    answer = []
    road = [[0] * columns for _ in range(rows)]
    temp = 1
    for i in range(rows):
        for j in range(columns):
            road[i][j] = temp
            temp += 1
    for x1, y1, x2, y2 in queries:
        road, min_num = rotate(road, x1, y1, x2, y2)
        answer.append(min_num)

    return answer

print(solution(rows, columns, queries))