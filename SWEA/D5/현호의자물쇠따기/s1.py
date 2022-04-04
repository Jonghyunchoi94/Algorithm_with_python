import sys
sys.stdin = open('input.txt')


def dfs(number, n, k, res):
    global cnt
    if number == n:
        if int(res) % k == 0:
            cnt += 1
        return

    for i in range(n):
        if i not in visited:
            visited.add(i)
            dfs(number + 1, n, k, res + num[i])
            visited.remove(i)



T = int(input())

for case in range(T):
    N = int(input())
    num = list(input().split())
    K = int(input())

    visited = set()
    cnt = 0
    dfs(0, N, K, '')
    print("#{} {}".format(case + 1, cnt))