import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    count = 0
    move = 1
    move_plus = 0
    while move_plus < distance:
        count += 1
        move_plus += move
        if count % 2 == 0:
            move += 1
    print(count)

