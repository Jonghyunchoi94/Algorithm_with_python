k = 3
score = [10, 100, 20, 150, 1, 100, 200]


def solution(k, score):
    answer = []

    n = len(score)
    temp = score[0]
    hof = []
    for i in range(n):
        if i < k:
            hof.append(score[i])
            if score[i] < temp:
                temp = score[i]
        else:
            if score[i] > temp:
                hof.append(score[i])
                hof.sort()
                hof.pop(0)
                temp = min(hof)
        answer.append(temp)

    return answer

print(solution(k, score))