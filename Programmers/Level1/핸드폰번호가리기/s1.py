phone_number = "01033334444"

def solution(phone_number):
    answer = ''
    len_star = len(phone_number) - 4
    answer = '*' * len_star + phone_number[-4:]
    return answer

print(solution(phone_number))