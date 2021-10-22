# 문제 읽기 : 5분
# 고려 사항 : 활주로는 일단 끊기면 안된다.
# ( 동일 행 혹은 열에서 경사로를 이용하든 이용하지 않든 자연스럽게 이어져야 한다.)


import sys
sys.stdin = open('input.txt')


def possible_road(cal_list):
    idx = 1
    pre = cal_list[0]
    while N > idx:
        cur = cal_list[idx]
        if pre == cur:
            pre = cal_list[idx]
            idx += 1
        elif abs(pre - cur) == 1:
            pass






T = int(input())

for case in range(T):
    N, X = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(N)]
    print(road)