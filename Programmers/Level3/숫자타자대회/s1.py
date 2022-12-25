numbers = "1756"

import sys
sys.setrecursionlimit(10**9)

phone = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
dict_phone = {}

for i in range(4):
    for j in range(3):
        dict_phone[phone[i][j]] = (i, j)

def solution(numbers):
    answer = 987654321
    def distance(vec1, vec2):
        weight = 1
        if abs(vec2[1] - vec1[1]) + abs(vec2[0] - vec1[0]) == 0:
            weight = 1
        elif abs(vec2[0] - vec1[0]) == 0:
            weight = 2 * abs(vec2[1] - vec1[1])
        elif abs(vec2[1] - vec1[1]) == 0:
            weight = 2 * abs(vec2[0] - vec1[0])
        else:
            weight = 3 * min(abs(vec2[0] - vec1[0]), abs(vec2[1] - vec1[1])) + 2 * abs(abs(vec2[0] - vec1[0]) - abs(vec2[1] - vec1[1]))

        return weight

    def dfs(r_hand, l_hand, n, res):
        nonlocal answer
        if res >= answer:
            return
        if n == len(numbers):
            answer = min(answer, res)
            return

        if dict_phone[numbers[n]] == r_hand or dict_phone[numbers[n]] == l_hand:
            dfs(r_hand, l_hand, n + 1, res + 1)
        else:
            dfs(dict_phone[numbers[n]], l_hand, n + 1, res + distance(r_hand, dict_phone[numbers[n]]))
            dfs(r_hand, dict_phone[numbers[n]], n + 1, res + distance(l_hand, dict_phone[numbers[n]]))

        return

    dfs(dict_phone['6'], dict_phone['4'], 0, 0)

    return answer

print(solution(numbers))