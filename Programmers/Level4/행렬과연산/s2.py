rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operations = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

from collections import deque

def rotate(original):
    l1 = deque(original[0][1: len(original[0]) - 1])
    l2 = deque([original[i][len(original[0]) - 1] for i in range(len(original))])
    l3 = deque(original[len(original) - 1][1: len(original[0]) - 1])
    l4 = deque([original[i][0] for i in range(len(original))])

    l2.appendleft(l1.pop())
    l3.append(l2.pop())
    l4.append(l3.popleft())
    l1.appendleft(l4.popleft())

    original[0][1: len(original[0]) - 1] = list(l1)
    original[len(original) - 1][1: len(original[0]) - 1] = list(l3)
    original[0:len(original)][0] = list(l4)
    for i in range(len(original)):
        original[i][len(original[0]) - 1] = list(l2)[i]
        original[i][0] = list(l4)[i]


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