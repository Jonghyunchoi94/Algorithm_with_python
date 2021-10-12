import sys
sys.stdin = open('input.txt')


def possible_score(number, score):
    if number == N:
        visited.add(score)
        return

    possible_score(number + 1, score)
    possible_score(number + 1, score + data[number])

T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    visited = set()

    possible_score(0, 0)
    print('#{} {}'.format(case + 1, len(visited)))