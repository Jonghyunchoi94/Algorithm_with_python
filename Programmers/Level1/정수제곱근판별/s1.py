n = 121

def solution(n):
    answer = 0
    if int(n ** 0.5) == n ** 0.5:
        answer = (int(n ** 0.5) + 1) ** 2
    else:
        answer = -1
    return answer

print(solution(n))