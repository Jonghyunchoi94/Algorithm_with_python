# 문제 파악 1차 : 5분

import sys
sys.stdin = open('input.txt')

from collections import defaultdict, deque

def dist(a , b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def stair_time(dict_list):
    sorted_zero = sorted(dict_list[0])
    sorted_one = sorted(dict_list[1])
    q_zero = deque()
    for i in range(len(sorted_zero) - 3):
        if sorted_zero[i + 3] - sorted_zero[i] < room[stairs[0][0]][stairs[0][1]]:
            sorted_zero[i + 3] += room[stairs[0][0]][stairs[0][1]]



def dfs(member, time):
    global ans
    if member == len(person):
        return

    dfs(member + 1, time[0].append(dist(person[member], stairs[0]) + room[stairs[0][0]][stairs[0][1]] + 1))
    dfs(member + 1, time[1].append(dist(person[member], stairs[1]) + room[stairs[1][0]][stairs[1][1]] + 1))



T = int(input())

for case in range(T):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stairs = []
    status = defaultdict(list)
    ans = 987654321
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                person.append((i, j))
            elif room[i][j] > 1:
                stairs.append((i, j))

    dfs(0, status)
