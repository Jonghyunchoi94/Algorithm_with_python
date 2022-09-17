import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    a, b, c = map(int, input().split())

    start = min(a, b)
    gcd = -1
    while start >= 1:

        if (a % start == 0) and (b % start == 0):
            gcd = max(gcd, start)
            break

        start -= 1

    print(gcd)
    if (gcd == 1) or (c % gcd == 0):
        print("YES")
    else:
        print("NO")
