import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n = int(input())
    zero, one = 1, 0

    for i in range(n):
        zero, one = one, zero + one

    print(zero, one)