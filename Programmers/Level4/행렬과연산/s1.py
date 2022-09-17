rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

from collections import deque

def rotate(original):
    res = [[0 for _ in range(len(original[0]))] for _ in range(len(original))]
    ch = []
    # 첫 행
    for i in range(1, len(original[0])):
        ch.append((0, i))
        res[0][i] = original[0][i - 1]

    # 끝 열
    for i in range(1, len(original)):
        ch.append((i, len(original[0]) - 1))
        res[i][len(original[0]) - 1] = original[i - 1][len(original[0]) - 1]

    # 끝 행
    for i in range(len(original[0])-2, -1, -1):
        ch.append((len(original) - 1, i))
        res[len(original) - 1][i] = original[len(original) - 1][i + 1]

    # 첫 열
    for i in range(len(original) - 2, -1, -1):
        ch.append((i, 0))
        res[i][0] = original[i + 1][0]

    for i, j in ch:
        original[i][j] = res[i][j]

    return original

def shiftrow(original):
    original = deque(original)
    original.appendleft(original.pop())
    return list(original)

def solution(rc, operations):
    answer = rc

    for i in operations:
        if i == "ShiftRow":
            answer = shiftrow(answer)
        elif i == "Rotate":
            answer = rotate(answer)

    return answer



print(solution(rc, operations))