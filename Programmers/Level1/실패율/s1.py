N = 4
stages = [4,4,4,4,4]

from collections import defaultdict

def solution(N, stages):
    answer = []
    ing = defaultdict(int)
    ed = defaultdict(int)
    fail = defaultdict(int)
    stages.sort(reverse=True)
    cnt = 0
    tmp = stages[0]
    for i in stages:
        if i != tmp:
            ing[i] += 1
            ed[i] += (cnt + 1)
        else:
            ing[i] += 1
            ed[i] += 1
        cnt = ed[i]
        tmp = i

    if ed[N + 1] and (not ed[N]):
        ed[N] += ed[N + 1]

    for i in range(1, N + 1):
        if i not in ed:
            ed[i] = 0
        if i not in ing:
            ing[i] = 0

        if ed[i] == 0 or ing[i] == 0:
            fail[i] = 0
        else:
            fail[i] = ing[i] / ed[i]


    sorted_fail = sorted(fail.items(), key=lambda x:x[1], reverse=True)

    for i, j in sorted_fail:
        answer.append(i)
    return answer

print(solution(N, stages))