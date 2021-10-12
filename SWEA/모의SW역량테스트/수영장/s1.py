import sys
sys.stdin = open('input.txt')

move = [1, 1, 3]

def dfs(month, money):
    global ans
    if money >= ans:
        return

    if month > 11:
        if ans > money:
            ans = money
        return

    dfs(month + move[0], money + (data[month] * fee[0]))
    dfs(month + move[1], money + fee[1])
    dfs(month + move[2], money + fee[2])

T = int(input())

for case in range(T):
    *fee, year = list(map(int, input().split()))
    data = list(map(int, input().split()))

    ans = 987654321

    dfs(0, 0)
    print('#{} {}'.format(case + 1, min(year, ans)))