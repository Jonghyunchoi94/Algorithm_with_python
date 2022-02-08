id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

from collections import defaultdict

def solution(id_list, report, k):
    # 시간초과 에러 해결! 아예 초장부터 형변환으로 중복을 제거하자!
    report = set(report)
    answer = []
    record = defaultdict(set)
    number = defaultdict(int)
    # 신고 요주 인물 색출
    for i in report:
        user, target = i.split()
        number[target] += 1

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

