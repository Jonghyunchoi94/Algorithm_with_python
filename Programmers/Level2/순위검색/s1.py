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

from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)

    for i in info:
        temp = i.split()
        field = temp[:-1]
        score = int(temp[-1])

        for j in range(5):
            combi = list(combinations(field, j))
            for k in combi:
                temp_field = ''.join(k)
                info_dict[temp_field].append(score)

    for key in info_dict:
        info_dict[key].sort()
    print(info_dict)
    for i in query:
        temp = i.replace("and", "")
        temp = temp.replace("-", "")
        temp = temp.split()
        field = temp[:-1]
        score = int(temp[-1])

        field = ''.join(field)

        if field in info_dict:
            scorelist = info_dict[field]

            if len(scorelist) > 0:
                start, end = 0, len(scorelist)
                while start < end:
                    mid = (start + end) // 2
                    if scorelist[mid] >= score:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scorelist) - start)
        # 5시간 동안 발견 못한 실수
        else:
            answer.append(0)

    return answer


print(solution(info, query))