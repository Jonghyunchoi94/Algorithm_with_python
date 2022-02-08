id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    record = defaultdict(set)
    number = defaultdict(int)
    temp_record = []
    # 신고 요주 인물 색출
    for i in report:
        user, target = i.split()
        if (user, target) not in temp_record:
            number[target] += 1
            temp_record.append((user, target))

    # 신고 대상자 발송
    for i in report:
        user, target = i.split()
        if number[target] >= k:
            record[user].add(target)

    for i in id_list:
        if i in record:
            answer.append(len(record[i]))
        else:
            answer.append(0)
    return answer


print(solution(id_list, report, k))

