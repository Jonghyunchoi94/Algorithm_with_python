import sys
sys.stdin = open('input.txt')


T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    possible_scores = [0] * (sum(data) + 1)
    possible_scores[0] = 1
    for i in data:
        for j in range(len(possible_scores)-1, -1, -1):
            if possible_scores[j] == 1:
                possible_scores[j + i] = 1

    print('#{} {}'.format(case + 1, possible_scores.count(1)))
