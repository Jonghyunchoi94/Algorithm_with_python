n = 7
k = 3
enemy = [4, 2, 4, 5, 3, 3, 1]

import heapq

def solution(n, k, enemy):
    answer = 0

    q = [(n, k, 0)]

    while q:
        soldier, chance, idx = heapq.heappop(q)



    return answer

print(solution(n, k, enemy))