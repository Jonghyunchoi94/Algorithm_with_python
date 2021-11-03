s = "one4seveneight"

num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
        # replace 메소드는 해당 문자열이 존재하지 않으면 자동으로 넘긴다.
    return int(answer)

print(solution(s))