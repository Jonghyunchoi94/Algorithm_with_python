import sys
sys.stdin = open('input.txt')

T = int(input())

def gcd(N, X) :
    while X > 0:
        N, X = X, N % X
    return N

for _ in range(T):
    a, b, c = map(int, input().split())

    gcd = gcd(a, b)

    print(gcd)
    if (gcd == 1) or (c % gcd == 0):
        print("YES")
    else:
        print("NO")