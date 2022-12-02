import sys
sys.stdin = open('input.txt')

T = int(input())


def fibo(n):
    global zero, one
    if n == 0:
        zero += 1
        return n
    elif n == 1:
        one += 1
        return n
    return fibo(n - 1) + fibo(n - 2)


for _ in range(T):
    n = int(input())
    zero, one = 0, 0
    fibo(n)
    print(zero, one)