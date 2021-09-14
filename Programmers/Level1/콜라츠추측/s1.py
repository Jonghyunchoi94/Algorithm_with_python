n = 6

def solution(num):
    answer = 0
    cnt = 0
    while num != 1:
        if cnt >= 500:
            answer = -1
            break
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2
        cnt += 1
    if num == 1:
        answer = cnt
    return answer


print(solution(n))