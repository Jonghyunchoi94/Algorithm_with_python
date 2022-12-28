n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

import sys

sys.setrecursionlimit(10 ** 9)


def solution(n, k, enemy):
    answer = 0

    def dfs(soldier, chance, n_round):
        nonlocal answer

        if soldier <= 0:
            if soldier == 0:
                answer = max(answer, n_round - 1)
            else:
                answer = max(answer, n_round - 2)
            return

        if n_round > len(enemy):
            answer = len(enemy)
            return

        if chance < k:
            dfs(soldier, chance + 1, n_round + 1)
            dfs(soldier - enemy[n_round - 1], chance, n_round + 1)
        else:
            dfs(soldier - enemy[n_round - 1], chance, n_round + 1)

        return

    dfs(n, 0, 1)

    return answer

print(solution(n, k, enemy))