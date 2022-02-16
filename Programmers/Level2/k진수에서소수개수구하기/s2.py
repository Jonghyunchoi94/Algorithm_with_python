n = 437674
k = 3

"""
- 0P0처럼 소수 양쪽에 0이 있는 경우
- P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
- 0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
- P처럼 소수 양쪽에 아무것도 없는 경우
- 단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
- 예를 들어, 101은 P가 될 수 없습니다.
"""

def encoding(n, k):
    answer = ''
    if k == 10:
        return str(n)
    while n > 0:
        answer += str(n % k)
        n //= k

    return answer[::-1]

def prime(num):
    Flag = True
    temp = 2

    if int(num) < 2:
        return False
    if int(num) == 2:
        return True

    while temp < (int(num) ** 0.5 + 1):
        if not(int(num) % temp):
            Flag = False
            break
        temp += 1
    return Flag

def primeRule(num):
    answer = 0
    num_list = num.split("0")

    for i in num_list:
        if i and prime(i):
            answer += 1

    return answer


def solution(n, k):
    answer = primeRule(encoding(n, k))

    return answer


print(solution(n, k))