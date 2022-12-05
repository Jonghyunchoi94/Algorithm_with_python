import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
'''
1 => 1
2 => 2 4 8 6
3 => 3 9 7 1
4 => 4 6
5 => 5
6 => 6
7 => 7 9 3 1
8 => 8 4 2 6
9 => 9 1

'''
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())

    a %= 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b %= 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b %= 4
        if b == 0:
            print((a ** 4) % 10)
        else:
            print((a ** b) % 10)
