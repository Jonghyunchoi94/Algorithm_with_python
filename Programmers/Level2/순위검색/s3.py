info = [
    "java backend junior pizza 150","python frontend senior chicken 210",
    "python frontend senior chicken 150","cpp backend senior pizza 260",
    "java backend junior chicken 80","python backend senior chicken 50"
]

query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

from collections import defaultdict
from itertools import combinations

def solution(info, query):
    answer = []

    store = defaultdict(list)

    for i in info:
        t = i.split(" ")
        c, s = t[:-1], int(t[-1])
        for j in range(5):
            case = list(combinations(c, j))
            for k in case:
                temp = "".join(k)
                store[temp].append(s)

    for key in store:
        store[key].sort()

    for q in query:
        t = q.replace("-", "")
        t = t.replace("and", "")
        t = t.split()
        c, s = t[:-1], int(t[-1])
        case = "".join(c)

        if case in store:
            scorelist = store[case]
            start, end = 0, len(scorelist)

            while start < end:
                mid = (start + end) // 2
                if scorelist[mid] >= s:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(scorelist) - start)
        else:
            answer.append(0)

    return answer

print(solution(info, query))