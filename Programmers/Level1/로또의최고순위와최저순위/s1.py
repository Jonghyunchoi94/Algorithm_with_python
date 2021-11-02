lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    max_match = 0
    min_match = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            max_match += 1
        elif lottos[i] in win_nums:
            max_match += 1
            min_match += 1
    res_max = 6
    res_min = 6
    if min_match > 0:
        res_min = (7 - min_match)
    if max_match > 0:
        res_max = (7 - max_match)
    answer = [res_max, res_min]
    return answer


print(solution(lottos, win_nums))