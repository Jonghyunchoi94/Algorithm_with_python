import sys
sys.stdin = open('input.txt')
T = int(sys.stdin.readline())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    res = factorial(M) / (factorial(M - N) * factorial(N))

    print(int(res))
