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

def switch_on(clocks, switch_num):
    for i in range(16):
        if linked[switch_num][i] == 1:
            clocks[i] += 3
            if clocks[i] == 15:
                clocks[i] = 3


def solve(clocks, switch_num):
    for i in range(4):
        switch_on(clocks, switch_num)

    return


C = int(input())

for case in range(C):
    clock = list(map(int, input().split()))

    print(solve(clock, 0))