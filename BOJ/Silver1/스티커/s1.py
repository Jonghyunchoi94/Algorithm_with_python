import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    s = []
    for _ in range(2):
        s.append(list(map(int, sys.stdin.readline().split())))

    if n == 1:
        print(max(s[0][n - 1], s[1][n - 1]))
    else:
        s[0][1] += s[1][0]
        s[1][1] += s[0][0]

        for i in range(2, n):
            s[0][i] += max(s[1][i - 1], s[1][i - 2])
            s[1][i] += max(s[0][i - 1], s[0][i - 2])

        print(max(s[0][n - 1], s[1][n - 1]))

