def solution(t, p):
    answer = 0

    m = len(t)
    n = len(p)

    for i in range(0, m - n + 1):
        temp = t[i: i + n]
        if int(p) >= int(temp):
            answer += 1

    return answer