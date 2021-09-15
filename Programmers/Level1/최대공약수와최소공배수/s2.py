"""
최대공약수와 최소공배수 간의 관계 이용

숫자 a, b가 있다고 가정하고
G = 최대공약수
L = 최소공배수   라고 할 때

L * G = a * b


참고용 풀이
"""
def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer