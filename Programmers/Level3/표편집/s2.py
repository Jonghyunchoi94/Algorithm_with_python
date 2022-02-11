n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

"""
연결리스트를 통해 효율성을 극대화합시다!
주의사항 : 변수를 업데이트 할 때 작동 순서에 주의합시다!
"""

from collections import defaultdict
def solution(n, k, cmd):
    answer = ["O"] * n
    cursor = k
    storage = defaultdict(list)
    last_idx = n - 1
    stack = []
    for i in range(n):
        if i == 0:
            storage[i] = [n - 1, i + 1]
        elif i == n - 1:
            storage[i] = [i - 1, 0]
        else:
            storage[i] = [i - 1, i + 1]
    for i in cmd:
        if len(i) != 1:
            direction, instance = i.split()
            if direction == "D":
                for _ in range(int(instance)):
                    cursor = storage[cursor][1]
            elif direction == "U":
                for _ in range(int(instance)):
                    cursor = storage[cursor][0]
        elif i == "C":
            prev, next = storage[cursor]
            stack.append([prev, next, cursor])
            answer[cursor] = "X"
            storage[prev][1] = next
            storage[next][0] = prev

            if cursor == last_idx:
                last_idx = storage[cursor][0]
                cursor = storage[cursor][0]
            else:
                cursor = storage[cursor][1]

        elif i == "Z":
            before, after, now = stack.pop()
            answer[now] = "O"
            storage[before][1] = now
            storage[after][0] = now

            if now > last_idx:
                last_idx = now

    answer = "".join(answer)

    return answer


print(solution(n, k, cmd))