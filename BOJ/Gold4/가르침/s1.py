from itertools import combinations
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())

basic = 'antic'

words = []
alpha = ''
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    t = word[4: -4]
    temp = ''
    for w in t:
        if (w not in basic) and (w not in temp):
            temp += w
        if (w not in basic) and (w not in alpha):
            alpha += w
    if len(temp) <= K - 5:
        words.append(temp)


def dfs(case, word, length):
    global Flag
    if length == len(word):
        Flag = True
        return
    if word[length] not in case:
        return

    dfs(case, word, length + 1)

    return


if K < 5:
    print(0)
elif K == 26:
    print(N)
else:
    case = list(combinations(alpha, K - 5))
    cnt = [0] * len(case)


    for i in range(len(case)):
        c = 0
        for j in words:
            Flag = False
            dfs(case[i], j, 0)
            if Flag:
                c += 1
        cnt[i] = c

    print(max(cnt))

