import sys
sys.stdin = open('input.txt')

from copy import deepcopy

def wheel(number, direction):
    if direction == 1:
        temp_data[number - 1].insert(0, temp_data[number - 1].pop())
    else:
        temp_data[number - 1].append(temp_data[number - 1].pop(0))

# 이 함수가 True이면 wheel 함수에서 움직임을 실시할 것이다.
def pair_wheel_plus_condition(number):
    if data[number - 1][6] != data[number - 2][2]:
        return True
    return False

def pair_wheel_minus_condition(number):
    if data[number - 1][2] != data[number][6]:
        return True
    return False


def change(number, direction):
    temp_plus = number + 1
    temp_minus = number - 1

    wheel(number, direction)
    direction1 = direction
    direction2 = direction

    while temp_minus >= 1:
        if pair_wheel_minus_condition(temp_minus):
            if direction1 == 1:
                wheel(temp_minus, -1)
                direction1 = -1
            else:
                wheel(temp_minus, 1)
                direction1 = 1
        else:
            break
        temp_minus -= 1

    while temp_plus <= 4:
        if pair_wheel_plus_condition(temp_plus):
            if direction2 == 1:
                wheel(temp_plus, -1)
                direction2 = -1
            else:
                wheel(temp_plus, 1)
                direction2 = 1
        else:
            break
        temp_plus += 1




T = int(input())

for case in range(T):
    K = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]

    temp_data = deepcopy(data)

    for t in range(K):
        n, d = map(int, input().split())
        change(n, d)
        data = deepcopy(temp_data)

    ans = 0

    for i in range(4):
        ans += (temp_data[i][0]) * (2 ** i)

    print('#{} {}'.format(case + 1, ans))
