# 문제 파악 : 5분 40초
# 문제 상 상하좌우 & 행렬 주의 !!


import sys
sys.stdin = open('input.txt')

dr = [0, -1, 0, 1, 0] # 가만히, 상, 우, 하, 좌
dc = [0, 0, 1, 0, -1]

# dr = [0, 0, 1, 0, -1] # 가만히, 좌, 하, 우, 상
# dc = [0, -1, 0, 1, 0]
def position_mark(c, r, distance, degree, number):
    for i in range(10):
        for j in range(10):
            if abs(c - j) + abs(r - i) <= distance:
                if (i, j) not in power:
                    power[(i, j)] = [degree]
                else:
                    power[(i, j)].append(degree)
                if (i, j) not in distribution:
                    distribution[(i, j)] = [k]
                else:
                    distribution[(i, j)].append(k)


T = int(input())

for case in range(T):
    M, A = map(int, input().split())
    user_A = list(map(int, input().split()))
    user_B = list(map(int, input().split()))
    data = [[0] * 10 for _ in range(10)]
    power = {}
    distribution = {}
    for k in range(A):
        column, row, C, P = map(int, input().split())
        position_mark(column - 1, row - 1, C, P, k)

    idx = 0
    userA_pos = [0, 0]
    userB_pos = [9, 9]
    while M >= idx:
        if (userA_pos[0], userA_pos[1]) in distribution and (userB_pos[0], userB_pos[1]) in distribution:
            if len(distribution[(userA_pos[0], userA_pos[1])]) == 1 and max(distribution[(userA_pos[0], userA_pos[1])]) in distribution[(userB_pos[0], userB_pos[1])]:
                data[userA_pos[0]][userA_pos[1]] += max(power[(userA_pos[0], userA_pos[1])])
                data[userB_pos[0]][userB_pos[1]] += (sum(power[(userB_pos[0], userB_pos[1])]) - max(power[(userA_pos[0], userA_pos[1])]))
            elif len(distribution[(userB_pos[0], userB_pos[1])]) == 1 and max(distribution[(userB_pos[0], userB_pos[1])]) in distribution[(userA_pos[0], userA_pos[1])]:
                data[userB_pos[0]][userB_pos[1]] += max(power[(userB_pos[0], userB_pos[1])])
                data[userA_pos[0]][userA_pos[1]] += (sum(power[(userA_pos[0], userA_pos[1])]) - max(power[(userB_pos[0], userB_pos[1])]))
            # elif len(distribution[(userA_pos[0], userA_pos[1])]) > 1 and len(distribution[(userB_pos[0], userB_pos[1])]) > 1:

            else:
                if len(power[(userA_pos[0], userA_pos[1])]) == 1:
                    data[userA_pos[0]][userA_pos[1]] += max(power[(userA_pos[0], userA_pos[1])])
                else:
                    data[userA_pos[0]][userA_pos[1]] += max(power[(userA_pos[0], userA_pos[1])])

                if len(power[(userB_pos[0], userB_pos[1])]) == 1:
                    data[userB_pos[0]][userB_pos[1]] += max(power[(userB_pos[0], userB_pos[1])])
                else:
                    data[userB_pos[0]][userB_pos[1]] += max(power[(userB_pos[0], userB_pos[1])])
        else:
            if (userA_pos[0], userA_pos[1]) in power and len(power[(userA_pos[0], userA_pos[1])]) == 1:
                data[userA_pos[0]][userA_pos[1]] += max(power[(userA_pos[0], userA_pos[1])])
            elif (userA_pos[0], userA_pos[1]) in power:
                data[userA_pos[0]][userA_pos[1]] += max(power[(userA_pos[0], userA_pos[1])])

            if (userB_pos[0], userB_pos[1]) in power and len(power[(userB_pos[0], userB_pos[1])]) == 1:
                data[userB_pos[0]][userB_pos[1]] += max(power[(userB_pos[0], userB_pos[1])])
            elif (userB_pos[0], userB_pos[1]) in power:
                data[userB_pos[0]][userB_pos[1]] += max(power[(userB_pos[0], userB_pos[1])])

        if idx < 20:
            userA_pos = [userA_pos[0] + dr[user_A[idx]], userA_pos[1] + dc[user_A[idx]]]
            userB_pos = [userB_pos[0] + dr[user_B[idx]], userB_pos[1] + dc[user_B[idx]]]
        idx += 1


    res = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] != 0:
                res += data[i][j]
    print(res)



