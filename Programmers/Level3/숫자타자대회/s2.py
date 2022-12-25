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
    dp = [{} for _ in range(len(numbers))]
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

    def dfs(n):
        if n == 0:
            dp[0][(numbers[n], "4")] = distance(dict_phone[numbers[n]], dict_phone["6"])
            dp[0][("6", numbers[n])] = distance(dict_phone[numbers[n]], dict_phone["4"])
            track = [(numbers[n], "4"), ("6", numbers[n])]
            return track

        track = []
        for i in dfs(n - 1):
            dp[n][(numbers[n], i[1])] = dp[n - 1][(i[0], i[1])] + distance(dict_phone[numbers[n]], dict_phone[i[0]])
            dp[n][(i[0], numbers[n])] = dp[n - 1][(i[0], i[1])] + distance(dict_phone[numbers[n]], dict_phone[i[1]])
            track.extend([(numbers[n], i[1]), (i[0], numbers[n])])
        return track


    candidate = dfs(len(numbers) - 1)

    for r, l in candidate:
        answer = min(answer, dp[len(numbers) - 1][(r, l)])
    return answer

print(solution(numbers))