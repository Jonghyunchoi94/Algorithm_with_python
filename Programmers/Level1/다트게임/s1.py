dartResult = "1D2S3T*"

def calc(str):
    if len(str) == 2:
        if str[1] == "S":
            return int(str[0])
        elif str[1] == "D":
            return int(str[0]) ** 2
        elif str[1] == "T":
            return int(str[0]) ** 3
    elif len(str) == 3:
        if str[2] == "S":
            return int(str[:2])
        elif str[2] == "D":
            return int(str[:2]) ** 2
        elif str[2] == "T":
            return int(str[:2]) ** 3


def solution(dartResult):
    temp_str = ""
    temp_ans = []
    for i in dartResult:
        if i.isdecimal():
            temp_str += i
        elif i.isalpha():
            temp_str += i
            # 디버깅 후 해결
            # 첫 점수가 0점일 때와 10점일 때 고려해줘야함
            # Testcase 5, 8번
            if len(temp_str) == 2:
                temp_ans.append(calc(temp_str[-2:]))
            elif temp_str[-2] == "0" and temp_str[-3].isdecimal():
                temp_ans.append(calc(temp_str[-3:]))
            else:
                temp_ans.append(calc(temp_str[-2:]))
        elif i == "#":
            temp_ans[-1] = -1 * temp_ans[-1]
        elif i == "*":
            if len(temp_ans) == 1:
                temp_ans[-1] = 2 * temp_ans[-1]
            elif len(temp_ans) > 1:
                temp_ans[-2] = 2 * temp_ans[-2]
                temp_ans[-1] = 2 * temp_ans[-1]

    answer = sum(temp_ans)
    return answer


print(solution(dartResult))