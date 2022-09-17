rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

from collections import deque

def solution(rc, operations):
    row, column = len(rc), len(rc[0])
    left, mid, right = deque(), deque(), deque()

    for r in range(row):
        left.append(rc[r][0])
        right.append(rc[r][-1])
        tmp = deque(rc[r][1: column - 1])
        mid.append(tmp)

    for op in operations:
        if op == "ShiftRow":
            tmp_row = mid.pop()
            mid.appendleft(tmp_row)
            x = left.pop()
            left.appendleft(x)
            y = right.pop()
            right.appendleft(y)
        elif op == "Rotate":
            x = left.popleft()
            mid[0].appendleft(x)
            x = mid[0].pop()
            right.appendleft(x)
            x = right.pop()
            mid[-1].append(x)
            x = mid[-1].popleft()
            left.append(x)
    answer = []

    for r in range(row):
        answer.append([])
        answer[-1].append(left.popleft())
        answer[-1].extend(mid.popleft())
        answer[-1].append(right.popleft())


    return answer

print(solution(rc, operations))