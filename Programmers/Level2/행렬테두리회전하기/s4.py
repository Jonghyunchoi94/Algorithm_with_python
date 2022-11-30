rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


def rotate(road, x1, y1, x2, y2):
    tmp = road[x1 - 1][y1 - 1]
    mini = tmp

    for k in range(x1 - 1, x2 - 1):
        test = road[k + 1][y1 - 1]
        road[k][y1 - 1] = test
        mini = min(mini, test)

    for k in range(y1 - 1, y2 - 1):
        test = road[x2 - 1][k + 1]
        road[x2 - 1][k] = test
        mini = min(mini, test)

    for k in range(x2 - 1, x1 - 1, -1):
        test = road[k - 1][y2 - 1]
        road[k][y2 - 1] = test
        mini = min(mini, test)

    for k in range(y2 - 1, y1 - 1, -1):
        test = road[x1 - 1][k - 1]
        road[x1 - 1][k] = test
        mini = min(mini, test)

    road[x1 - 1][y1] = tmp

    return road, mini

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