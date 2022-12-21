from itertools import combinations
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
ans = 0
res = 0
def change(word):
    ans = []
    for w in word:
        ans.append(ord(w) - ord('a'))
    return ans


if K >= 5:
    num = set()
    data = []
    for _ in range(N):
        t = change(set(sys.stdin.readline().rstrip()[4: -4]) - {'a', 'n', 't', 'i', 'c'})
        if len(t) == 0:
            res += 1
            continue

        num |= set(t)
        data.append(t)

    for i, r in enumerate(data):
        q = 0
        for a in r:
            q |= (1 << a)
        data[i] = q

    temp = 0
    temp |= 1 << (ord('a') - ord('a'))
    temp |= 1 << (ord('n') - ord('a'))
    temp |= 1 << (ord('t') - ord('a'))
    temp |= 1 << (ord('i') - ord('a'))
    temp |= 1 << (ord('c') - ord('a'))

    if len(num) < K - 5:
        print(N)
    else:
        for i in combinations(num, K - 5):
            c = temp
            cnt = 0
            for j in i:
                if not c & (1 << j):
                    c |= 1 << j

            c ^= (1<<26) - 1
            for d in data:
                if d & c == 0:
                    cnt += 1
            ans = max(ans, cnt)
        print(ans + res)
else:
    print(0)


