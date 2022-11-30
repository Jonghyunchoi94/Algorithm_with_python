k = 3
score = [10, 100, 20, 150, 1, 100, 200]

import heapq
def solution(k, score):
    answer = []

    n = len(score)
    temp = score[0]
    hof = []
    for i in range(n):
        if i < k:
            heapq.heappush(hof, score[i])
            if score[i] < temp:
                temp = score[i]
        else:
            if score[i] > temp:
                heapq.heappush(hof, score[i])
                heapq.heappop(hof)
                temp = hof[0]
        answer.append(temp)

    return answer

print(solution(k, score))