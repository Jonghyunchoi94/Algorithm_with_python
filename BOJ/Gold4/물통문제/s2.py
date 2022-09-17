import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    cnt = 0
    while a != 0 and b != 0:
        if a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2
            cnt += 1
        elif a % 2 and b % 2 == 0:
            b //= 2
        elif a % 2 == 0 and b % 2:
            a //= 2
        else:
            if a > b:
                a -= b
            else:
                b -= a

    n = max(a, b)

    gcd = (2 ** cnt) * n

    if (gcd == 1) or (c % gcd == 0):
        print("YES")
    else:
        print("NO")