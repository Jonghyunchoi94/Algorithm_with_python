orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

"""
["AC", "ACDE", "BCFG", "CDE"]
"""

from itertools import combinations
from collections import defaultdict




def solution(orders, course):
    answer = []
    sort_orders = ["".join(sorted(i)) for i in orders]
    print(sort_orders)
    sort_orders = sorted(sort_orders, key=len)
    print(sort_orders)

    storage = defaultdict(int)
    tmp_storage = defaultdict(int)

    for i in sort_orders:
        tmp_len = len(i)
        Flag = False
        while tmp_len > 1:
            tmp_str = combinations(i, tmp_len)
            for j in tmp_str:
                if "".join(j) not in storage:
                    storage["".join(j)] += 1
                else:
                    Flag = True
                    storage["".join(j)] += 1
            if Flag:
                break
            tmp_len -= 1
    print(storage)

    return answer

print(solution(orders, course))