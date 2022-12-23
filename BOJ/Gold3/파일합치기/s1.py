import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())

for _ in range(T):
    K = int(sys.stdin.readline())
    data = [0] + list(map(int, sys.stdin.readline().split()))
    S = [0 for _ in range(K + 1)]
    for i in range(1, K + 1):
        S[i] = S[i - 1] + data[i]

    print(S)

    dp = [[0] * (len(data) + 1)for _ in range(len(data) + 1)]


    print(dp)