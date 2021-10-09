import sys
sys.stdin = open('input.txt')

h=[50000,10000,5000,1000,500,100,50,10]

T = int(input())

for case in range(T):
    N = int(input())
    res = []
    idx = 0
    while len(h) > idx:
        res.append(N//h[idx])
        N %= h[idx]
        idx += 1

    print('#{}'.format(case + 1))
    print(' '.join(map(str, res)))