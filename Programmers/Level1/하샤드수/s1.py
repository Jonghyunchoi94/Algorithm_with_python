arr = 10


def solution(x):
    answer = True
    sum_num = 0
    for i in str(x):
        sum_num += int(i)

    if x % sum_num != 0:
        answer = False

    return answer

print(solution(arr))