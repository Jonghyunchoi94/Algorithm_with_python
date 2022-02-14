places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

"""
[1, 0, 1, 1, 1]
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(places):
    testcase = len(places)
    answer = [0] * testcase

    def warning(x, y, distance, data, visited, Flag):
        nonlocal sign
        if distance == 2:
            if Flag:
                sign = True
            return
        if Flag:
            sign = True
            return

        for k in range(4):
            next_x = x + dx[k]
            next_y = y + dy[k]
            if 0 <= next_x < 5 and 0 <= next_y < 5 and (next_x, next_y) not in visited:
                if data[next_x][next_y] == "O":
                    visited.add((next_x, next_y))
                    warning(next_x, next_y, distance + 1, data, visited, False)
                elif data[next_x][next_y] == "P":
                    visited.add((next_x, next_y))
                    warning(next_x, next_y, distance + 1, data, visited, True)

    for i in range(testcase):
        sign = False
        for r in range(5):
            for c in range(5):
                if places[i][r][c] == "P":
                    warning(r, c, 0, places[i], {(r, c)}, False)
                    if sign:
                        break
            if sign:
                break
        if sign:
            answer[i] = 0
        else:
            answer[i] = 1


    return answer

print(solution(places))