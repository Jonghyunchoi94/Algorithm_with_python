num = 3

def solution(num):
    answer = ''
    if num%2==0:
        answer='Even'
    else:
        answer='Odd'
    return answer

print(solution(num))