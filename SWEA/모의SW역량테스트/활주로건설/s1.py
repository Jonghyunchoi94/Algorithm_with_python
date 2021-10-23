# 문제 읽기 : 5분
# 고려 사항 : 활주로는 일단 끊기면 안된다.
# ( 동일 행 혹은 열에서 경사로를 이용하든 이용하지 않든 자연스럽게 이어져야 한다.)


import sys
sys.stdin = open('input.txt')


def possible_road(cal_list):
    idx = 1
    pre = cal_list[0]
    check = []
    while N > idx:
        cur = cal_list[idx]
        if pre == cur:
            pre = cal_list[idx]
            idx += 1
        elif pre - cur == 1:
            if idx + X - 1 < N:
                for k in range(1, X):
                    if cal_list[idx + k] != cur:
                        return False
                else:
                    check.extend(range(idx, idx + X))
                    pre = cal_list[idx + X - 1]
                    idx += X
            else:
                return False
        elif cur - pre == 1:
            if idx - X >= 0:
                for k in range(2, X + 1):
                    if cal_list[idx - k] != pre:
                        return False
                else:
                    for i in range(idx - X, idx):
                        if i in check:
                            return False
                    else:
                        check.extend(range(idx - X, idx))
                        pre = cal_list[idx]
                        idx += 1
            else:
                return False
        else:
            return False
    return True



T = int(input())

for case in range(T):
    N, X = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    road_zip = list(zip(*road))

    cnt = 0
    for i in road:
        if possible_road(i):
            cnt += 1

    for i in road_zip:
        if possible_road(i):
            cnt += 1
    print('#{} {}'.format(case + 1, cnt))