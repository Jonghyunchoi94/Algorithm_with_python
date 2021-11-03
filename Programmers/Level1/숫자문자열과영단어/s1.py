s = "one4seveneight"

number_info = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def solution(s):
    answer = ''
    tmp = ''
    idx = 0
    while len(s) > idx:
        if tmp in number_info:
            answer += str(number_info[tmp])
            tmp = ''

        if s[idx].isdecimal():
            answer += str(s[idx])
        else:
            tmp += s[idx]
        idx += 1

    if tmp in number_info:
        answer += str(number_info[tmp])

    return int(answer)

print(solution(s))