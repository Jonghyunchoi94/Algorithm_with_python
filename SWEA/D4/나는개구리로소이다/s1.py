import sys
sys.stdin = open('input.txt')

from collections import deque

word = {
        'c': 0,
        'r': 1,
        'o': 2,
        'a': 3,
        'k': 4,
    }

T = int(input())

for case in range(T):
    s = deque(input())
    answer = 0
    empty_list = [-1 for _ in range(len(s) // 5)]
    visited = [False] * (len(s) // 5)
    # 예외 처리
    if len(s) % 5:
        answer = -1

    else:
        while s:
            output_str = s.popleft()

            for i in range(len(empty_list)):
                if word[output_str] == (empty_list[i] + 1):
                    visited[i] = True
                    empty_list[i] += 1
                    if empty_list[i] == 4:
                        empty_list[i] = -1
                    break
            else:
                answer = -1
                break

    if answer != -1:
        answer = visited.count(True)

    print("#{} {}".format(case + 1, answer))
    # print(empty_list)
    # print(visited)

