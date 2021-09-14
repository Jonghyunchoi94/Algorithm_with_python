x = 2
n = 5

"""
- 세 가지 조건 분기
0일 때
0보다 클 때
0보다 작을 때 

"""


def solution(x, n):
    answer = []
    if x > 0:
        for i in range(x, (x*n)+1, x):
            answer.append(i)
    elif x < 0:
        for i in range(x, (x*n)-1, x):
            answer.append(i)
    else:
        answer = [0] * n
    return answer

print(solution(x, n))