n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
# ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]

# 시간 오류 및 일부 테스트 케이스 오류


from collections import defaultdict

def solution(n, k, cmd):
    answer = ["O"] * n
    cursor = k
    storage = defaultdict(list)
    stack = []
    for i in range(n):
        storage[i].extend([i, 1])

    for i in cmd:
        if len(i) != 1:
            direction, instance = i.split()
            if direction == "D":
                cursor = (cursor + int(instance)) % n
            elif direction == "U":
                cursor = (cursor - int(instance)) % n
        elif i == "C":
            for idx in storage:
                if storage[idx][0] == cursor and storage[idx][1] == 1:
                    stack.append(idx)
                    storage[idx][1] = 0
                if storage[idx][0] > cursor:
                    storage[idx][0] -= 1
            n -= 1
            if cursor > n - 1:
                cursor = n - 1
        elif i == "Z":
            num = stack.pop()
            for idx in storage:
                if idx == num and storage[idx][1] == 0:
                    storage[idx][1] = 1
                if idx > num:
                    storage[idx][0] += 1
            n += 1
            if cursor > num:
                cursor += 1

    for i in stack:
        answer[i] = "X"

    answer = "".join(answer)


    return answer

print(solution(n, k, cmd))