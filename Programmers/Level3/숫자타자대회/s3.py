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
    n = len(numbers)
    def distance(vec1, vec2):
        if abs(vec2[1] - vec1[1]) + abs(vec2[0] - vec1[0]) == 0:
            weight = 1
        elif abs(vec2[0] - vec1[0]) == 0:
            weight = 2 * abs(vec2[1] - vec1[1])
        elif abs(vec2[1] - vec1[1]) == 0:
            weight = 2 * abs(vec2[0] - vec1[0])
        else:
            weight = 3 * min(abs(vec2[0] - vec1[0]), abs(vec2[1] - vec1[1])) + 2 * abs(abs(vec2[0] - vec1[0]) - abs(vec2[1] - vec1[1]))
        return weight

    dp = [[[-1] * 10 for _ in range(10)] for _ in range(n)]

    def dfs(r_hand, l_hand, cnt):
        if cnt == n:
            return 0

        if dp[cnt][int(r_hand)][int(l_hand)] != -1:
            return dp[cnt][int(r_hand)][int(l_hand)]
        result = 987654321
        if numbers[cnt] != r_hand:
            result = min(result, dfs(r_hand, numbers[cnt], cnt + 1) + distance(dict_phone[numbers[cnt]], dict_phone[l_hand]))

        if numbers[cnt] != l_hand:
            result = min(result, dfs(numbers[cnt], l_hand, cnt + 1) + distance(dict_phone[numbers[cnt]], dict_phone[r_hand]))

        dp[cnt][int(r_hand)][int(l_hand)] = result

        return result

    dfs("6", "4", 0)
    for i in range(10):
        for j in range(10):
            if dp[0][i][j] == -1:
                continue
            answer = min(answer, dp[0][i][j])
    return answer

print(solution(numbers))