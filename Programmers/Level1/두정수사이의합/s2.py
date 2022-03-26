def solution(a, b):
    answer = 0
    if a == b:
        answer = a

    elif a < b:
        while a <= b:
            if a == b:
                answer += a
                break
            answer += a
            answer += b
            a += 1
            b -= 1

    else:
        while a >= b:
            if a == b:
                answer += a
                break
            answer += a
            answer += b
            a -= 1
            b += 1
    return answer