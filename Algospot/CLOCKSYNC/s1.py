import sys
sys.stdin = open('input.txt')

linked = [
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1),
    (1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0),
    (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1),
    (0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0),
]


def allpass(clocks):
    for i in range(16):
        if clocks[i] != 12:
            return False
    else:
        return True


def switch_on(clocks, switch_num):
    for i in range(16):
        if linked[switch_num][i] == 1:
            clocks[i] += 3
            if clocks[i] == 15:
                clocks[i] = 3


def solve(clocks, switch_num):
    if switch_num == 10:
        if not allpass(clocks):
            return sys.maxsize
        else:
            return 0

    ret = sys.maxsize
    for cnt in range(4):
        ret = min(ret, cnt + solve(clocks, switch_num + 1))
        switch_on(clocks, switch_num)

    return ret


C = int(input())

for case in range(C):
    clock = list(map(int, input().split()))

    print(solve(clock, 0))