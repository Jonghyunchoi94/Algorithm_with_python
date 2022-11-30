s =  "xababcdcdababcdcd"


def short(s, num):
    ans = s[:num]
    temp = 0
    res = ""
    for i in range(0,len(s),num):
        if s[i: i + num] == ans:
            temp += 1
        else:
            if temp == 1:
                res += ans
            else:
                res += str(temp)
                res += ans
            temp = 1
            ans = s[i: i + num]
    if temp == 1:
        res += ans
    else:
        res += str(temp)
        res += ans
    return res

def solution(s):
    answer = 987654321
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        # print(short(s, i))
        if answer > len(short(s, i)):
            answer = len(short(s, i))

    return answer

print(solution(s))