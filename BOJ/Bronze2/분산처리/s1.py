import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    # print(str(a**b)[-1])
    print((a**b) % 10)