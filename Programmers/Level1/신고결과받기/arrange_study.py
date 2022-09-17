id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report = set(report)
    report_storage = defaultdict(int)
    email_storage = defaultdict(list)

    for w in report:
        a, b = w.split()
        report_storage[b] += 1

    for r in report:
        a, b = r.split()
        if report_storage[b] >= k:
            email_storage[a].append(b)

    for id in id_list:
        answer.append(len(email_storage[id]))

    # print(report_storage)
    # print(email_storage)



    return answer

print(solution(id_list, report, k))