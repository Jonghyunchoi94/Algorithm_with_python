n = 5
build_frame = [
    [0,0,0,1],[2,0,0,1],[4,0,0,1],
    [0,1,1,1],[1,1,1,1],[2,1,1,1],
    [3,1,1,1],[2,0,0,0],[1,1,1,0],
    [2,2,0,1]
]

from collections import defaultdict

def solution(n, build_frame):
    answer = []
    store = defaultdict(int)

    for x, y, a, b in build_frame:
        if b == 0:
            if a == 0:
                if store[(x + 1, y, 0)] > 0 and (not(store[(x, y + 1, 1)] > 0 or store[(x, y - 1, 1)] > 0)):
                    continue
                store[(x, y, a)] -= 1
            elif a == 1:
                if (not(store[(x, y - 1, 0)] > 0 or store[(x + 1, y - 1, 0)]> 0)) and (not(store[(x - 1, y, 1)] > 0 and store[(x + 1, y, 1)] > 0)):
                    continue
                store[(x, y, a)] -= 1

        else:
            if a == 0:
                if y == 0:
                    store[(x, y, a)] += 1
                    continue
                elif store[(x, y - 1, 0)] <= 0 and (not(store[(x - 1, y, 1)] > 0 or store[(x, y, 1)] > 0)):
                    continue
                store[(x, y, a)] += 1
            elif a == 1:
                if (not(store[(x, y - 1, 0)] > 0 or store[(x + 1, y - 1, 0)] > 0)) and (not(store[(x - 1, y, 1)] > 0 and store[(x + 1, y, 1)])):
                    continue
                store[(x, y, a)] += 1

    for x, y, a in store:
        if store[(x, y, a)] > 0:
            answer.append([x, y, a])

    answer.sort()

    # print(store)

    return answer

print(solution(n, build_frame))