orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

"""
["AC", "ACDE", "BCFG", "CDE"]
"""

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for i in course:
        storage = []
        for j in orders:
            if len(j) >= i:
                tmp = combinations(j, i)
                for k in tmp:
                    storage.append("".join(sorted(k)))
        storage_count = Counter(storage).most_common()
        answer += [menu for menu, cnt in storage_count if cnt > 1 and cnt == storage_count[0][1]]
    answer.sort()
    return answer

print(solution(orders, course))