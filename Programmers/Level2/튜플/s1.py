s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"


def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)
    print(s)

    for i in s:
        temp = i.split(",")
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))

    return answer

print(solution(s))